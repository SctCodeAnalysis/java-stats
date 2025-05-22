"""
Module for the number of files metric.
"""

from typing import List

from ..parser import ParsedFile
from .metric import Metric


class NumberOfJavaFiles(Metric):
    """
    Calculate the number of Java files.
    """

    def __init__(self):
        self.count = 0

    def compute(self, files: List[ParsedFile]):
        self.count = len(files)

    def result(self) -> float:
        return self.count
