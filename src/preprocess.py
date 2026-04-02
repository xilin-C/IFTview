"""Signal preprocessing utilities.

This module is responsible for optional signal cleanup steps before peak
detection, such as smoothing, normalization, or baseline correction.
"""

from .config import PreprocessConfig


def preprocess_signal(
    x_values: list[float],
    y_values: list[float],
    config: PreprocessConfig,
) -> tuple[list[float], list[float]]:
    """Apply preprocessing to the raw signal.

    Args:
        x_values: Original x-axis values.
        y_values: Original intensity values.
        config: Preprocessing settings.

    Returns:
        Processed x/y values ready for downstream modules.

    TODO:
    - Implement optional smoothing.
    - Implement optional baseline correction.
    - Implement optional normalization.
    """

    return x_values, y_values

