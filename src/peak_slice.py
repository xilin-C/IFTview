"""Single-peak slicing logic.

This module extracts one peak window from the full signal using a detected
peak position and a slicing strategy.
"""

from dataclasses import dataclass

from .config import SliceConfig
from .peak_detect import PeakCandidate


@dataclass
class PeakSlice:
    """Container for one extracted peak window."""

    peak_id: int
    start_index: int
    end_index: int
    x_values: list[float]
    y_values: list[float]


def slice_peak(
    x_values: list[float],
    y_values: list[float],
    peak: PeakCandidate,
    config: SliceConfig,
) -> PeakSlice:
    """Extract a single peak around the detected peak center.

    TODO:
    - Support valley-based boundary detection.
    - Support fixed-window slicing as a fallback.
    - Guard against overlapping or out-of-range slices.
    """

    raise NotImplementedError("TODO: implement single-peak slicing.")


def slice_all_peaks(
    x_values: list[float],
    y_values: list[float],
    peaks: list[PeakCandidate],
    config: SliceConfig,
) -> list[PeakSlice]:
    """Extract all detected peaks from the full signal.

    TODO:
    - Define overlap handling between neighboring peaks.
    - Add optional per-peak diagnostics.
    """

    raise NotImplementedError("TODO: implement batch peak slicing.")

