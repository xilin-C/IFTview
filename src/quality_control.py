"""Quality control checks for detected peaks, slices, and IFT outputs.

This module is intended to hold lightweight validation logic so the pipeline
can flag suspicious peaks without mixing QC into algorithm modules.
"""

from dataclasses import dataclass, field

from .ift_core import IFTResult
from .peak_detect import PeakCandidate
from .peak_slice import PeakSlice


@dataclass
class QCReport:
    """Simple quality-control report for one pipeline stage."""

    peak_id: int | None
    passed: bool
    messages: list[str] = field(default_factory=list)


def check_detected_peaks(peaks: list[PeakCandidate]) -> QCReport:
    """Run basic checks on the full set of detected peaks.

    TODO:
    - Validate peak count against the expected target.
    - Flag duplicate or unsorted peak positions.
    """

    raise NotImplementedError("TODO: implement peak-detection QC.")


def check_peak_slice(peak_slice: PeakSlice) -> QCReport:
    """Run basic checks on one sliced peak.

    TODO:
    - Validate slice width and non-empty data.
    - Flag suspicious boundary placement.
    """

    raise NotImplementedError("TODO: implement peak-slice QC.")


def check_ift_result(result: IFTResult) -> QCReport:
    """Run basic checks on one IFT result.

    TODO:
    - Validate output shape and finite values.
    - Add domain-specific sanity checks once the expected result is defined.
    """

    raise NotImplementedError("TODO: implement IFT QC.")

