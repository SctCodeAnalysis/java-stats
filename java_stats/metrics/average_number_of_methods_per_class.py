"""
Class for calculating average number of methods per class.
"""

from typing import List

import javalang

from ..parser import ParsedFile
from .metric import Metric


class AverageNumberOfMethodsPerClass(Metric):
    """
    Calculate the average number of methods per class.
    """

    def __init__(self):
        self.total_methods = 0
        self.total_classes = 0

    def compute(self, files: List[ParsedFile]):
        for file in files:
            for class_decl in file.structure.filter(javalang.tree.ClassDeclaration):
                class_node = class_decl[1]
                self.total_methods += len(class_node.methods)
                self.total_classes += 1

    def result(self) -> float:
        if self.total_classes == 0:
            return 0.0
        return self.total_methods / self.total_classes
