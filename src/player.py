"""Playback utilities for automatically showing generated results.

This module should provide a lightweight replay mechanism that displays the
generated paired figures in sequence.
"""

from pathlib import Path

from .config import VisualizationConfig


def autoplay_figures(figure_paths: list[Path], config: VisualizationConfig) -> None:
    """Automatically play a sequence of generated figures.

    TODO:
    - Choose the MVP playback approach.
    - Add pause/resume or loop support if needed later.
    """

    raise NotImplementedError("TODO: implement autoplay for result figures.")

