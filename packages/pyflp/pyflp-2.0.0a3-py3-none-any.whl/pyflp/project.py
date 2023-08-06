# PyFLP - An FL Studio project file (.flp) parser
# Copyright (C) 2022 demberto
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details. You should have received a copy of the
# GNU General Public License along with this program. If not, see
# <https://www.gnu.org/licenses/>.

"""Contains the types used by the public API and other project-wide properties."""

from __future__ import annotations

import datetime
import enum
import math
import pathlib
import sys
from typing import cast

if sys.version_info >= (3, 8):
    from typing import Final, TypedDict
else:
    from typing_extensions import Final, TypedDict

if sys.version_info >= (3, 11):
    from typing import Unpack
else:
    from typing_extensions import Unpack

import construct as c
import construct_typed as ct

from ._descriptors import EventProp, KWProp
from ._events import (
    DATA,
    DWORD,
    TEXT,
    WORD,
    AnyEvent,
    AsciiEvent,
    BoolEvent,
    EventEnum,
    I16Event,
    I32Event,
    StructEventBase,
    U8Event,
    U32Event,
)
from ._models import FLVersion, MultiEventModel
from .arrangement import (
    ArrangementID,
    Arrangements,
    ArrangementsID,
    TimeMarkerID,
    TrackID,
)
from .channel import ChannelID, ChannelRack, DisplayGroupID, RackID
from .exceptions import ExpectedValue, PropertyCannotBeSet, UnexpectedType
from .mixer import InsertID, Mixer, MixerID, SlotID
from .pattern import PatternID, Patterns, PatternsID
from .plugin import PluginID

_DELPHI_EPOCH: Final = datetime.datetime(1899, 12, 30)
MIN_TEMPO: Final = 10.000
VALID_PPQS: Final = (24, 48, 72, 96, 120, 144, 168, 192, 384, 768, 960)

__all__ = ["PanLaw", "Project", "FileFormat", "VALID_PPQS"]


class TimestampEvent(StructEventBase):
    STRUCT = c.Struct("created_on" / c.Float64l, "time_spent" / c.Float64l).compile()


@enum.unique
class PanLaw(ct.EnumBase):
    """Used by :attr:`Project.pan_law`."""

    Circular = 0
    Triangular = 2


@enum.unique
class FileFormat(enum.IntEnum):
    """File formats used by FL Studio.

    *New in FL Studio v2.5.0*: FST (FL Studio state) file format.
    """

    None_ = -1
    """Temporary file."""

    Project = 0
    """FL Studio project (.flp)."""

    Score = 0x10
    """FL Studio score (.fsc). Stores pattern notes and controller events."""

    Automation = 24
    """Stores controller events and automation channels as FST."""

    ChannelState = 0x20
    """Entire channel (including plugin events). Stored as FST."""

    PluginState = 0x30
    """Events of a native plugin on a channel or insert slot. Stored as FST."""

    GeneratorState = 0x31
    """Plugins events of a VST instrument. Stored as FST."""

    FXState = 0x32
    """Plugin events of a VST effect. Stored as FST."""

    InsertState = 0x40
    """Insert and all its slots. Stored as FST."""

    _ProbablyPatcher = 0x50  # TODO Patcher presets are stored as `PluginState`.


class ProjectID(EventEnum):
    LoopActive = (9, BoolEvent)  # TODO Is this for patterns or arrangements?
    ShowInfo = (10, BoolEvent)
    _Volume = (12, U8Event)
    PanLaw = (23, U8Event)
    Licensed = (28, BoolEvent)
    _TempoCoarse = WORD + 2
    Pitch = (WORD + 16, I16Event)
    _TempoFine = WORD + 29  #: 3.4.0+
    CurGroupId = (DWORD + 18, I32Event)
    Tempo = (DWORD + 28, U32Event)
    FLBuild = (DWORD + 31, U32Event)
    Title = TEXT + 2
    Comments = TEXT + 3
    Url = TEXT + 5
    _RTFComments = TEXT + 6  #: 1.2.10+
    FLVersion = (TEXT + 7, AsciiEvent)
    Licensee = TEXT + 8  #: 1.3.9+
    DataPath = TEXT + 10  #: 9.0+
    Genre = TEXT + 14  #: 5.0+
    Artists = TEXT + 15  #: 5.0+
    Timestamp = (DATA + 29, TimestampEvent)


class _ProjectKW(TypedDict):
    channel_count: int
    ppq: int
    format: FileFormat


class Project(MultiEventModel):
    """Represents an FL Studio project."""

    def __init__(self, *events: AnyEvent, **kw: Unpack[_ProjectKW]):
        super().__init__(*events, **kw)

    def __repr__(self) -> str:
        return f"FL Studio {str(self.version)} {self.format.name}"

    def _collect_events(self, *enums: type[EventEnum]):
        for event in self._events_tuple:
            for enum_ in enums:
                if event.id in enum_:
                    yield event
                    break

    @property
    def arrangements(self) -> Arrangements:
        """Provides an iterator over arrangements and other related properties."""
        arrnew_occured = False
        filtered_events: list[AnyEvent] = []
        for event in self._collect_events(
            ArrangementID, ArrangementsID, TrackID, TimeMarkerID
        ):
            if event.id == ArrangementID.New:
                arrnew_occured = True

            # * Prevents accidentally passing on Pattern's timemarkers
            # TODO This logic will still be incorrect if arrangement's
            # timemarkers occur before ArrangementID.New event.
            elif event.id in TimeMarkerID and not arrnew_occured:
                continue
            filtered_events.append(event)

        return Arrangements(*filtered_events, version=self.version)

    artists = EventProp[str](ProjectID.Artists)
    """Authors / artists info. to be embedded in exported WAV & MP3.

    *New in FL Studio v5.0.*
    """

    @property
    def channel_count(self) -> int:
        """Number of channels in the rack.

        For Patcher presets, the total number of plugins used inside it.

        Raises:
            ValueError: When a value less than zero is tried to be set.
        """
        return self._kw["channel_count"]

    @channel_count.setter
    def channel_count(self, value: int):
        if value < 0:
            raise ValueError("Channel count cannot be less than zero")
        self._kw["channel_count"] = value

    @property
    def channels(self) -> ChannelRack:
        """Provides an iterator over channels and channel rack properties."""
        events: list[AnyEvent] = []

        if RackID.WindowHeight in self._events:
            events.append(self._events[RackID.WindowHeight][0])

        for event in self._events_tuple:
            if event.id == InsertID.Flags:
                break

            for enum_ in (ChannelID, DisplayGroupID, PluginID, RackID):
                if event.id in enum_:
                    events.append(event)
                    break

        return ChannelRack(*events, channel_count=self.channel_count)

    comments = EventProp[str](ProjectID.Comments, ProjectID._RTFComments)
    """Comments / project description / summary.

    Caution:
        Very old versions of FL used to store comments in RTF (Rich Text Format).
        PyFLP makes no efforts to parse that and stores it like a normal string
        as it is. It is upto you to extract the text out of it.
    """

    # Stored as a duration in days since the Delphi epoch (30 Dec, 1899).
    @property
    def created_on(self) -> datetime.datetime | None:
        """The local date and time on which this project was created."""
        if ProjectID.Timestamp in self._events:
            event = cast(TimestampEvent, self._events[ProjectID.Timestamp][0])
            return _DELPHI_EPOCH + datetime.timedelta(days=event["created_on"])

    format = KWProp[FileFormat]()
    """Internal format marker used by FL Studio to distinguish between types."""

    @property
    def data_path(self) -> pathlib.Path | None:
        """The absolute path used by FL to store all your renders.

        *New in FL Studio v9.0.0.*
        """
        if ProjectID.DataPath in self._events:
            event = self._events[ProjectID.DataPath][0]
            return pathlib.Path(event.value)

    @data_path.setter
    def data_path(self, value: str | pathlib.Path):
        if ProjectID.DataPath not in self._events:
            raise PropertyCannotBeSet(ProjectID.DataPath)

        if isinstance(value, pathlib.Path):
            value = str(value)

        path = "" if value == "." else value
        self._events[ProjectID.DataPath][0].value = path

    genre = EventProp[str](ProjectID.Genre)
    """Genre of the song to be embedded in exported WAV & MP3.

    *New in FL Studio v5.0*.
    """

    licensed = EventProp[bool](ProjectID.Licensed)
    """Whether the project was last saved with a licensed copy of FL Studio.

    Tip:
        Setting this to `True` and saving back the FLP will make it load the
        next time in a trial version of FL if it wouldn't open before.
    """

    # Internally, this is jumbled up. Thanks to @codecat/libflp for decode algo.
    @property
    def licensee(self) -> str | None:
        """The license holder's username who last saved the project file.

        If saved with a trial version this is empty.

        Tip:
            As of the latest version, FL doesn't check for the contents of
            this for deciding whether to open or not when in trial version.

        *New in FL Studio v1.3.9*.
        """
        events = self._events.get(ProjectID.Licensee)
        if events is not None:
            event = events[0]
            licensee = bytearray()
            for idx, char in enumerate(event.value):
                c1 = ord(char) - 26 + idx
                c2 = ord(char) + 49 + idx
                for num in c1, c2:
                    if chr(num).isalnum():
                        licensee.append(num)
                        break

            return licensee.decode("ascii")

    @licensee.setter
    def licensee(self, value: str):
        if ProjectID.Licensee not in self._events:
            raise PropertyCannotBeSet(ProjectID.Licensee)

        event = self._events[ProjectID.Licensee][0]
        licensee = bytearray()
        for idx, char in enumerate(value):
            c1 = ord(char) + 26 - idx
            c2 = ord(char) - 49 - idx
            for cp in c1, c2:
                if 0 < cp <= 127:
                    licensee.append(cp)
                    break
        event.value = licensee.decode("ascii")

    looped = EventProp[bool](ProjectID.LoopActive)
    """Whether a portion of the playlist is selected."""

    main_pitch = EventProp[int](ProjectID.Pitch)
    main_volume = EventProp[int](ProjectID._Volume)
    """*Changed in FL Studio v1.7.6*: Can be upto 125% (+5.6dB) now."""

    @property
    def mixer(self) -> Mixer:
        """Provides an iterator over inserts and other mixer related properties."""
        events: list[AnyEvent] = []
        inserts_began = False
        for event in self._events_tuple:
            # * Cannot use self._collect_events to first gather these and add
            # * PluginID events later; as it breaks the order of occurence.
            if event.id in (*MixerID, *InsertID, *SlotID):
                # TODO Find a more reliable to detect when inserts start.
                inserts_began = True
                events.append(event)

            if inserts_began and event.id in PluginID:
                events.append(event)

        return Mixer(*events, version=self.version)

    @property
    def patterns(self) -> Patterns:
        """Provides an iterator over patterns and other related properties."""
        return Patterns(*self._collect_events(PatternsID, PatternID))

    pan_law = EventProp[PanLaw](ProjectID.PanLaw)
    """Whether a circular or a triangular pan law is used for the project."""

    @property
    def ppq(self) -> int:
        """Pulses per quarter.

        Note:
            All types of lengths, positions and offsets internally use the PPQ
            as a multiplying factor.

        Danger:
            Don't try to set this property, it affects all the length, position
            and offset calculations used for deciding the placement of playlist,
            automations, timemarkers and patterns.

            When you change this in FL, it recalculates all the above. It is
            beyond PyFLP's scope to properly recalculate the timings.

        Raises:
            ExpectedValue: When a value not in `VALID_PPQS` is tried to be set.

        *Changed in FL Studio v2.1.1*: Defaults to 96.
        """
        return self._kw["ppq"]

    @ppq.setter
    def ppq(self, value: int):
        if value not in VALID_PPQS:
            raise ExpectedValue(value, VALID_PPQS)
        self._kw["ppq"] = value

    show_info = EventProp[bool](ProjectID.ShowInfo)
    """Whether to show a banner while the project is loading inside FL Studio.

    The banner shows the :attr:`title`, :attr:`artists`, :attr:`genre`,
    :attr:`comments` and :attr:`url`.
    """

    title = EventProp[str](ProjectID.Title)
    """Name of the song / project."""

    # Stored internally as the actual BPM * 1000 as an integer.
    @property
    def tempo(self) -> int | float | None:
        """Tempo at the current position of the playhead (in BPM).

        Raises:
            UnexpectedType: When a fine-tuned tempo (float) isn't supported.
                Use an `int` (coarse tempo) value.
            PropertyCannotBeSet: If underlying event isn't found.
            ValueError: When a tempo outside the allowed range is set.

        * *Changed in FL Studio v1.4.2*: Max tempo increased to 999 (int).
        * *New in FL Studio v3.4.0*: Fine tuned tempo (a float).
        * *Changed in FL Studio v11*: Max tempo limited to 522.000.
        """
        if ProjectID.Tempo in self._events:
            return self._events[ProjectID.Tempo][0].value / 1000

        tempo = None
        if ProjectID._TempoCoarse in self._events:
            tempo = self._events[ProjectID._TempoCoarse][0].value
        if ProjectID._TempoFine in self._events:
            tempo += self._events[ProjectID._TempoFine][0].value / 1000
        return tempo

    @tempo.setter
    def tempo(self, value: int | float):
        if self.tempo is None:
            raise PropertyCannotBeSet(
                ProjectID.Tempo, ProjectID._TempoCoarse, ProjectID._TempoFine
            )

        max_tempo = (
            999.000
            if self.version >= FLVersion(1, 4, 2) and self.version < FLVersion(11)
            else 522.000
        )

        if isinstance(value, float) and self.version < FLVersion(3, 4, 0):
            raise UnexpectedType(int, float)

        if float(value) > max_tempo or float(value) < MIN_TEMPO:
            raise ValueError(f"Invalid tempo {value}; expected {MIN_TEMPO}-{max_tempo}")

        if ProjectID.Tempo in self._events:
            self._events[ProjectID.Tempo][0].value = int(value * 1000)

        if ProjectID._TempoFine in self._events:
            tempo_fine = int((value - math.floor(value)) * 1000)
            self._events[ProjectID._TempoFine][0].value = tempo_fine

        if ProjectID._TempoCoarse in self._events:
            self._events[ProjectID._TempoCoarse][0].value = math.floor(value)

    @property
    def time_spent(self) -> datetime.timedelta | None:
        """Time spent on the project since its creation.

        Technically, since the last reset via FL's interface.
        """
        if ProjectID.Timestamp in self._events:
            event = cast(TimestampEvent, self._events[ProjectID.Timestamp][0])
            return datetime.timedelta(days=event["time_spent"])

    url = EventProp[str](ProjectID.Url)

    # Internally represented as a string with a format of
    # `major.minor.patch.build?` *where `build` is optional, since older
    # versions of FL didn't follow the same versioning scheme*.
    #
    # To maintain backward compatibility with FL Studio prior to v11.5 which
    # stored strings in ASCII, this event is always stored with ASCII data,
    # even if the rest of the strings use Windows Unicode (UTF16).
    @property
    def version(self) -> FLVersion:
        """The version of FL Studio which was used to save the file.

        Caution:
            Changing this to a lower version will not make a file load magically
            inside FL Studio, as newer events and/or plugins might have been used.

        Raises:
            PropertyCannotBeSet: This error should NEVER occur; if it does,
                it indicates possible corruption.
            ExpectedValue: When a string with an invalid format is tried to be set.
        """
        events = self._events[ProjectID.FLVersion]
        event = cast(AsciiEvent, events[0])
        return FLVersion(*tuple(int(part) for part in event.value.split(".")))

    @version.setter
    def version(self, value: FLVersion | str | tuple[int, ...]):
        if ProjectID.FLVersion not in self._events:
            raise PropertyCannotBeSet(ProjectID.FLVersion)

        if isinstance(value, FLVersion):
            parts = [value.major, value.minor, value.patch]
            if value.build is not None:
                parts.append(value.build)
        elif isinstance(value, str):
            parts = [int(part) for part in value.split(".")]
        else:
            parts = list(value)

        if len(parts) < 3 or len(parts) > 4:
            raise ExpectedValue("Expected format: major.minor.build.patch?")

        version = ".".join(str(part) for part in parts)
        self._events[ProjectID.FLVersion][0].value = version
        if len(parts) == 4 and ProjectID.FLBuild in self._events:
            self._events[ProjectID.FLBuild][0].value = parts[3]
