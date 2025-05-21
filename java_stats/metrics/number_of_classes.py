"""
Module for the number of classes metric.
"""

from typing import List

import javalang

from ..parser import ParsedFile
from .metric import Metric


class NumberOfClasses(Metric):
    """
    Calculate the number of classes in a Java repository.
    """

    def __init__(self):
        self.count = 0

    def compute(self, files: List[ParsedFile]):
        for file in files:
            self.count += len([file.structure.filter(javalang.tree.ClassDeclaration)])

    def result(self) -> float:
        return self.count
