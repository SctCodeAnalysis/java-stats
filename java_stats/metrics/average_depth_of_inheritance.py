"""
Class for calculating average depth of inheritance.
"""

from typing import List

from ..parser import ParsedFile
from .inheritance_utils import compute_all_depths
from .metric import Metric


class AverageDepthOfInheritance(Metric):
    """
    Calculate the average depth of inheritance tree.
    """

    def __init__(self):
        self.total_depth = 0
        self.total_classes = 0

    def compute(self, files: List[ParsedFile]):
        class_depths = compute_all_depths(files)
        self.total_depth = sum(class_depths.values())
        self.total_classes = len(class_depths)

    def result(self) -> float:
        if self.total_classes == 0:
            return 0.0
        return self.total_depth / self.total_classes
