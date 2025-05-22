"""
Class for calculating maximum depth of inheritance.
"""

from typing import List

from ..parser import ParsedFile
from .inheritance_utils import compute_all_depths
from .metric import Metric


class MaximumDepthOfInheritance(Metric):
    """
    Calculate the maximum depth of inheritance tree.
    """

    def __init__(self):
        self.max_depth = 0

    def compute(self, files: List[ParsedFile]):
        class_depths = compute_all_depths(files)
        self.max_depth = max(class_depths.values()) if class_depths else 0

    def result(self) -> float:
        return self.max_depth
