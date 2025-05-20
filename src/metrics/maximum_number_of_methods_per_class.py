"""
Class for the maximum number of methods per class metric.
"""

import javalang
from src.metrics.metric import Metric
from src.parser import ParsedFile


class MaximumNumberOfMethodsPerClass(Metric):
    """
    Calculate the maximum number of methods per class.
    """

    def __init__(self):
        self.max_methods = 0

    def compute(self, files: list[ParsedFile]):
        for file in files:
            for class_decl in file.structure.filter(javalang.tree.ClassDeclaration):
                class_node = class_decl[1]
                self.max_methods = max(self.max_methods, len(class_node.methods))

    def result(self) -> float:
        return self.max_methods
