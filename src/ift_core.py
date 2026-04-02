"""Inverse Fourier transform interfaces.

This module should contain the core IFT entry points that operate on one
sliced peak at a time and return structured transform results.
"""

from dataclasses import dataclass

from .peak_slice import PeakSlice


@dataclass
class IFTResult:
    """Container for the output of one IFT computation."""

    peak_id: int
    x_values: list[float]
    y_values: list[float]
    metadata: dict[str, float | int | str]


def run_ift(peak_slice: PeakSlice) -> IFTResult:
    """Run IFT for one sliced peak.

    TODO:
    - Confirm the exact numerical IFT method.
    - Define required preprocessing specific to IFT input.
    - Add error handling for invalid peak slices.
    """

    raise NotImplementedError("TODO: implement IFT for a single peak.")

