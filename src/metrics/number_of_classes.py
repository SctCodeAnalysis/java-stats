"""
Module for the number of classes metric.
"""

from typing import List
import javalang
from src.metrics.metric import Metric
from src.parser import ParsedFile


class NumberOfClasses(Metric):
    """
    Calculate the number of classes in a Java repository.
    """

    def __init__(self):
        self.count = 0

    def compute(self, files: List[ParsedFile]):
        """
        Calculate the number of classes in a Java repository.
        """
        for file in files:
            self.count += len([file.structure.filter(javalang.tree.ClassDeclaration)])


    def result(self) -> float:
        return self.count
