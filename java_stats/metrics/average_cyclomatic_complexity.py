"""
Class for calculating average cyclomatic complexity.
"""

from typing import List

import javalang

from ..parser import ParsedFile
from .metric import Metric
from .utils import calculate_cyclomatic_complexity, process_java_files


class AverageCyclomaticComplexity(Metric):
    """
    Calculate the average cyclomatic complexity of the methods.
    """

    def __init__(self):
        self.total_complexity = 0.0
        self.total_methods = 0

    def compute(self, files: List[ParsedFile]):
        def process_method(method: javalang.tree.MethodDeclaration):
            complexity = calculate_cyclomatic_complexity(method)
            self.total_complexity += complexity
            self.total_methods += 1

        process_java_files(files, process_method)

    def result(self) -> float:
        if self.total_methods == 0:
            return 0.0
        return self.total_complexity / self.total_methods
