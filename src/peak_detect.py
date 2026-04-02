"""Automatic peak detection interfaces.

This module should detect candidate reflection peaks from a preprocessed
signal and provide their positions for later slicing.
"""

from dataclasses import dataclass

from .config import DetectionConfig


@dataclass
class PeakCandidate:
    """Minimal description of a detected peak."""

    peak_id: int
    index: int
    x: float
    y: float


def detect_peaks(
    x_values: list[float],
    y_values: list[float],
    config: DetectionConfig,
) -> list[PeakCandidate]:
    """Detect reflection peaks from the full signal.

    TODO:
    - Choose the initial detection method for the MVP.
    - Add ranking or filtering to approach the expected 232 peaks.
    - Add confidence metrics for quality control.
    """

    raise NotImplementedError("TODO: implement peak detection.")

