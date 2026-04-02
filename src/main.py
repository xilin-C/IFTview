"""Command-line entry point for the IFTview MVP.

This file should stay thin: parse user input, build configuration, and call
the pipeline entry point.
"""

from pathlib import Path

from .config import build_default_config
from .pipeline import run_pipeline


def main() -> None:
    """Launch the default pipeline run.

    TODO:
    - Replace the placeholder input path with CLI argument parsing.
    - Add helpful error messages for missing input data.
    """

    config = build_default_config()
    input_file = config.paths.raw_dir / "sample_peaks.csv"
    run_pipeline(Path(input_file), config)


if __name__ == "__main__":
    main()

