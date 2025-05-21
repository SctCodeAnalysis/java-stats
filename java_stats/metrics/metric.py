"""
Base class for all metrics.
"""

from typing import List

from ..parser import ParsedFile


class Metric:
    """
    Base class for all metrics.
    """

    def compute(self, files: List[ParsedFile]):
        """
        Calculate the metric value.
        """

    def result(self) -> float:
        """Returns the result of the metric."""
        return 0.0
