"""Project configuration models and default settings.

This module centralizes the parameters used across the MVP pipeline so that
thresholds, file paths, and runtime options do not get scattered across files.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class PathConfig:
    """Filesystem locations used by the project."""

    project_root: Path = Path(__file__).resolve().parent.parent
    data_dir: Path = project_root / "data"
    raw_dir: Path = data_dir / "raw"
    output_dir: Path = data_dir / "output"
    figures_dir: Path = output_dir / "figures"
    slices_dir: Path = output_dir / "slices"
    ift_dir: Path = output_dir / "ift"


@dataclass
class DetectionConfig:
    """Parameters for peak detection."""

    expected_peak_count: int = 232
    min_peak_height: float | None = None
    min_peak_distance: int | None = None
    prominence: float | None = None


@dataclass
class SliceConfig:
    """Parameters for single-peak slicing."""

    use_valley_boundary: bool = True
    fixed_window_points: int | None = None
    padding_points: int = 0


@dataclass
class PreprocessConfig:
    """Parameters for signal preprocessing."""

    enable_smoothing: bool = False
    smoothing_window: int = 5
    enable_baseline_correction: bool = False
    enable_normalization: bool = False


@dataclass
class VisualizationConfig:
    """Parameters for figure generation and playback."""

    save_figures: bool = True
    show_figures: bool = False
    autoplay_interval_ms: int = 500
    figure_dpi: int = 150


@dataclass
class AppConfig:
    """Top-level application configuration."""

    paths: PathConfig = field(default_factory=PathConfig)
    preprocess: PreprocessConfig = field(default_factory=PreprocessConfig)
    detection: DetectionConfig = field(default_factory=DetectionConfig)
    slicing: SliceConfig = field(default_factory=SliceConfig)
    visualization: VisualizationConfig = field(default_factory=VisualizationConfig)


def build_default_config() -> AppConfig:
    """Return the default configuration for the MVP pipeline.

    TODO:
    - Add support for loading config from a file.
    - Add validation for inconsistent parameter combinations.
    """

    return AppConfig()

