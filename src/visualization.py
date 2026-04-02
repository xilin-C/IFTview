"""Figure generation for peak and IFT results.

This module should build the paired visual output for each peak:
the original peak view and the corresponding IFT result view.
"""

from pathlib import Path

from .config import VisualizationConfig
from .ift_core import IFTResult
from .peak_slice import PeakSlice


def create_peak_ift_figure(
    peak_slice: PeakSlice,
    ift_result: IFTResult,
    config: VisualizationConfig,
) -> object:
    """Create the paired figure for one peak and its IFT result.

    Returns:
        A figure-like object. The exact type will depend on the plotting
        library selected for the MVP.

    TODO:
    - Select the plotting library and return type.
    - Define figure layout, labels, and styling conventions.
    """

    raise NotImplementedError("TODO: implement figure creation.")


def save_figure(figure: object, output_path: Path, config: VisualizationConfig) -> Path:
    """Save a generated figure to disk.

    TODO:
    - Support the chosen plotting backend.
    - Standardize file naming for replay and inspection.
    """

    raise NotImplementedError("TODO: implement figure saving.")

