"""
Class for calculating average lines of code.
"""

from typing import List

import javalang

from ..parser import ParsedFile
from .metric import Metric
from .utils import count_method_lines, process_java_files


class AverageLinesOfCode(Metric):
    """
    Calculate the average lines of code per method.
    """

    def __init__(self):
        self.total_lines = 0.0
        self.total_methods = 0

    def compute(self, files: List[ParsedFile]):
        def process_method(method: javalang.tree.MethodDeclaration):
            lines = count_method_lines(files[0], method)
            self.total_lines += lines
            self.total_methods += 1

        for file in files:
            process_java_files([file], process_method)

    def result(self) -> float:
        if self.total_methods == 0:
            return 0.0
        return self.total_lines / self.total_methods
