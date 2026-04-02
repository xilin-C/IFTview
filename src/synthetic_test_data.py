"""Synthetic signal generation for pipeline structure testing.

This module generates a configurable distance-domain test signal with multiple
separable peaks and optional light noise. The goal is not physical realism;
it is to provide stable input for validating the program flow:
peak detection, peak slicing, IFT, and visualization.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import csv
import random


@dataclass
class PeakSpec:
    """Configuration for one synthetic peak.

    Attributes:
        center: Peak center position on the x-axis.
        width: Peak width parameter. In this simplified generator it is the
            Gaussian sigma.
        height: Peak amplitude above the baseline.
    """

    center: float
    width: float
    height: float


@dataclass
class SyntheticSignalConfig:
    """Configuration for building a synthetic multi-peak test signal."""

    x_start: float = 0.0
    x_end: float = 100.0
    num_points: int = 2000
    baseline: float = 0.0
    noise_level: float = 0.02
    random_seed: int = 7
    peaks: list[PeakSpec] = field(
        default_factory=lambda: [
            PeakSpec(center=12.0, width=1.2, height=1.0),
            PeakSpec(center=28.0, width=1.8, height=0.7),
            PeakSpec(center=43.0, width=1.0, height=1.3),
            PeakSpec(center=61.0, width=2.0, height=0.9),
            PeakSpec(center=82.0, width=1.4, height=1.1),
        ]
    )


@dataclass
class SyntheticSignal:
    """Container for synthetic signal data and its generation metadata.

    Attributes:
        x_values: Distance-domain x-axis values.
        y_values: Signal intensity values.
        peak_specs: Peak definitions used to build the signal.
        noise_level: Uniform noise level used in generation.
    """

    x_values: list[float]
    y_values: list[float]
    peak_specs: list[PeakSpec]
    noise_level: float

    def as_xy_tuple(self) -> tuple[list[float], list[float]]:
        """Return data in the same shape used by the rest of the pipeline.

        This mirrors the planned `load_signal()` output:
        `(x_values, y_values)`.
        """

        return self.x_values, self.y_values


def generate_distance_axis(x_start: float, x_end: float, num_points: int) -> list[float]:
    """Generate an evenly spaced x-axis for the synthetic signal.

    TODO:
    - Extend to non-uniform grids only if later algorithms require it.
    """

    if num_points < 2:
        raise ValueError("num_points must be at least 2.")

    step = (x_end - x_start) / (num_points - 1)
    return [x_start + index * step for index in range(num_points)]


def generate_synthetic_signal(config: SyntheticSignalConfig | None = None) -> SyntheticSignal:
    """Create a synthetic distance-domain signal with multiple peaks.

    The signal is a sum of Gaussian-like peaks over an optional constant
    baseline plus light uniform noise.

    Args:
        config: Signal generation settings. If omitted, a default test signal
            with several well-separated peaks is created.

    Returns:
        A `SyntheticSignal` object containing x/y data and metadata.
    """

    config = config or SyntheticSignalConfig()
    rng = random.Random(config.random_seed)
    x_values = generate_distance_axis(config.x_start, config.x_end, config.num_points)

    y_values: list[float] = []
    for x_value in x_values:
        signal_value = config.baseline
        for peak in config.peaks:
            signal_value += _gaussian_peak(x_value, peak)

        if config.noise_level > 0.0:
            signal_value += rng.uniform(-config.noise_level, config.noise_level)

        y_values.append(signal_value)

    return SyntheticSignal(
        x_values=x_values,
        y_values=y_values,
        peak_specs=list(config.peaks),
        noise_level=config.noise_level,
    )


def save_synthetic_signal_csv(signal: SyntheticSignal, output_path: Path) -> Path:
    """Save synthetic data as a simple two-column CSV.

    The CSV layout is intentionally straightforward so it can be consumed by a
    later `load_signal()` implementation without extra conversion:
    `x,y`
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["x", "y"])
        for x_value, y_value in zip(signal.x_values, signal.y_values):
            writer.writerow([x_value, y_value])

    return output_path


def build_default_synthetic_csv(output_path: Path) -> Path:
    """Generate and save the default synthetic test dataset.

    This helper is the simplest bridge between synthetic generation and the
    future file-based pipeline.
    """

    signal = generate_synthetic_signal()
    return save_synthetic_signal_csv(signal, output_path)


def run_basic_synthetic_test() -> SyntheticSignal:
    """Run the smallest non-GUI self-test for this module.

    The function generates the default signal, validates basic dimensions, and
    returns the generated data so callers can inspect or forward it.
    """

    signal = generate_synthetic_signal()

    if len(signal.x_values) != len(signal.y_values):
        raise RuntimeError("Synthetic signal generation produced mismatched x/y lengths.")

    if not signal.peak_specs:
        raise RuntimeError("Synthetic signal generation produced no peaks.")

    return signal


def _gaussian_peak(x_value: float, peak: PeakSpec) -> float:
    """Return the contribution of one simplified Gaussian peak.

    This internal helper keeps the main generator readable.
    """

    exponent = -((x_value - peak.center) ** 2) / (2.0 * peak.width ** 2)
    return peak.height * (2.718281828459045 ** exponent)


if __name__ == "__main__":
    default_output = Path(__file__).resolve().parent.parent / "data" / "raw" / "synthetic_signal.csv"
    signal = run_basic_synthetic_test()
    saved_path = save_synthetic_signal_csv(signal, default_output)

    print(f"Synthetic signal generated: {len(signal.x_values)} points")
    print(f"Configured peaks: {len(signal.peak_specs)}")
    print(f"Noise level: {signal.noise_level}")
    print(f"Saved CSV: {saved_path}")
