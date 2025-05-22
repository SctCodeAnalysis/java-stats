"""
Class for calculating maximum lines of code.
"""

from typing import List

import javalang

from ..parser import ParsedFile
from .metric import Metric
from .utils import count_method_lines, process_java_files


class MaximumLinesOfCode(Metric):
    """
    Calculate the maximum lines of code per method.
    """

    def __init__(self):
        self.max_lines = 0

    def compute(self, files: List[ParsedFile]):
        def process_method(method: javalang.tree.MethodDeclaration):
            lines = count_method_lines(files[0], method)
            self.max_lines = max(self.max_lines, lines)

        for file in files:
            process_java_files([file], process_method)

    def result(self) -> int:
        return self.max_lines
