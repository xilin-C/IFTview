"""Input/output helpers for loading data and saving pipeline artifacts.

This module should contain all filesystem-facing helpers so the rest of the
pipeline can focus on domain logic instead of path handling.
"""

from pathlib import Path
from typing import Iterable

from .config import PathConfig


def ensure_directories(paths: PathConfig) -> None:
    """Create required project directories if they do not exist.

    TODO:
    - Add logging for created vs existing directories.
    """

    required_dirs: Iterable[Path] = (
        paths.data_dir,
        paths.raw_dir,
        paths.output_dir,
        paths.figures_dir,
        paths.slices_dir,
        paths.ift_dir,
    )
    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)


def load_signal(file_path: Path) -> tuple[list[float], list[float]]:
    """Load the raw signal data from disk.

    Args:
        file_path: Path to the input file containing the signal.

    Returns:
        A pair of arrays/lists for the x-axis and y-axis data.

    TODO:
    - Decide the MVP input format (CSV, TXT, etc.).
    - Validate column count and missing values.
    - Replace placeholder return values with parsed data.
    """

    raise NotImplementedError("TODO: implement raw signal loading.")


def save_peak_slice(peak_id: int, x_values: list[float], y_values: list[float], output_dir: Path) -> Path:
    """Save one sliced peak to disk.

    TODO:
    - Decide the output format for sliced peak data.
    - Include metadata such as source file and detected boundaries.
    """

    raise NotImplementedError("TODO: implement sliced peak export.")


def save_ift_result(peak_id: int, x_values: list[float], y_values: list[float], output_dir: Path) -> Path:
    """Save one IFT result to disk.

    TODO:
    - Define a stable schema for IFT output files.
    - Add metadata needed for downstream QC and replay.
    """

    raise NotImplementedError("TODO: implement IFT result export.")

