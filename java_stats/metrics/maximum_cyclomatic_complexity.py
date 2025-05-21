"""
Class for calculating maximum cyclomatic complexity.
"""

from typing import List

import javalang

from ..parser import ParsedFile
from .metric import Metric
from .utils import calculate_cyclomatic_complexity


class MaximumCyclomaticComplexity(Metric):
    """
    Calculate the maximum cyclomatic complexity.
    """

    def __init__(self):
        self.max_complexity = 0

    def compute(self, files: List[ParsedFile]):
        if not files:
            self.max_complexity = 0
            return

        for file in files:
            tree = file.structure
            for _, class_node in tree.filter(javalang.tree.ClassDeclaration):
                for method in class_node.methods:
                    complexity = calculate_cyclomatic_complexity(method)
                    self.max_complexity = max(self.max_complexity, complexity)

    def result(self) -> float:
        return self.max_complexity
