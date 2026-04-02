"""High-level MVP pipeline orchestration.

This module wires together all project stages while keeping algorithm details
inside their own modules. It should become the single place that defines the
end-to-end processing order.
"""

from pathlib import Path

from .config import AppConfig
from .ift_core import run_ift
from .io_utils import ensure_directories, load_signal, save_ift_result, save_peak_slice
from .peak_detect import detect_peaks
from .peak_slice import slice_all_peaks
from .player import autoplay_figures
from .preprocess import preprocess_signal
from .quality_control import check_detected_peaks, check_ift_result, check_peak_slice
from .range_transform import transform_signal_range
from .visualization import create_peak_ift_figure, save_figure


def run_pipeline(input_file: Path, config: AppConfig) -> None:
    """Run the full MVP workflow from raw signal to optional autoplay.

    TODO:
    - Replace placeholder control flow with real algorithm calls.
    - Add structured logging for each pipeline stage.
    - Decide whether failures should stop the run or skip bad peaks.
    """

    ensure_directories(config.paths)

    x_values, y_values = load_signal(input_file)
    x_values, y_values = preprocess_signal(x_values, y_values, config.preprocess)
    x_values, y_values = transform_signal_range(x_values, y_values)

    peaks = detect_peaks(x_values, y_values, config.detection)
    check_detected_peaks(peaks)

    peak_slices = slice_all_peaks(x_values, y_values, peaks, config.slicing)

    figure_paths: list[Path] = []
    for peak_slice in peak_slices:
        check_peak_slice(peak_slice)

        save_peak_slice(
            peak_id=peak_slice.peak_id,
            x_values=peak_slice.x_values,
            y_values=peak_slice.y_values,
            output_dir=config.paths.slices_dir,
        )

        ift_result = run_ift(peak_slice)
        check_ift_result(ift_result)

        save_ift_result(
            peak_id=ift_result.peak_id,
            x_values=ift_result.x_values,
            y_values=ift_result.y_values,
            output_dir=config.paths.ift_dir,
        )

        figure = create_peak_ift_figure(peak_slice, ift_result, config.visualization)
        figure_path = config.paths.figures_dir / f"peak_{peak_slice.peak_id:03d}.png"
        save_figure(figure, figure_path, config.visualization)
        figure_paths.append(figure_path)

    if config.visualization.show_figures:
        autoplay_figures(figure_paths, config.visualization)

