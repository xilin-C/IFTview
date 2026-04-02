"""Coordinate and range transformation helpers.

This module is reserved for transforming input data ranges before slicing or
IFT, for example converting coordinate systems or normalizing peak windows.
"""


def transform_signal_range(x_values: list[float], y_values: list[float]) -> tuple[list[float], list[float]]:
    """Transform the raw signal into the range expected by later modules.

    TODO:
    - Clarify whether the project needs q-space, 2theta, or another domain.
    - Add reversible transforms when the required physics is finalized.
    """

    return x_values, y_values


def transform_peak_range(x_values: list[float], y_values: list[float]) -> tuple[list[float], list[float]]:
    """Transform a single sliced peak before IFT.

    TODO:
    - Define the exact peak-domain transform requirements for the MVP.
    - Add validation for invalid or empty peak windows.
    """

    return x_values, y_values

