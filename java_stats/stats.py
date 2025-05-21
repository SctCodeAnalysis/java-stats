"""
Class for calculating Java metrics.
"""

import xml.etree.ElementTree as ET
from datetime import datetime

from java_stats.metrics import (AverageCyclomaticComplexity,
                                AverageDepthOfInheritance, AverageLinesOfCode,
                                AverageNumberOfMethodsPerClass,
                                MaximumCyclomaticComplexity,
                                MaximumDepthOfInheritance, MaximumLinesOfCode,
                                MaximumNumberOfMethodsPerClass,
                                NumberOfClasses, NumberOfJavaFiles)
from java_stats.parser import parse_java_files


class JavaStats:
    """
    Class for calculating Java metrics.
    """

    def __init__(self, repo_path: str):
        """
        Initialize the JavaStats object.
        """
        self.repo_path = repo_path
        self.files = parse_java_files(self.repo_path)

        metrics = {
            "NUMBER_OF_JAVA_FILES": NumberOfJavaFiles,
            "NUMBER_OF_CLASSES": NumberOfClasses,
            "AVERAGE_NUMBER_OF_METHODS_PER_CLASS": AverageNumberOfMethodsPerClass,
            "MAXIMUM_NUMBER_OF_METHODS_PER_CLASS": MaximumNumberOfMethodsPerClass,
            "AVERAGE_CYCLOMATIC_COMPLEXITY": AverageCyclomaticComplexity,
            "MAXIMUM_CYCLOMATIC_COMPLEXITY": MaximumCyclomaticComplexity,
            "AVERAGE_LINES_OF_CODE": AverageLinesOfCode,
            "MAXIMUM_LINES_OF_CODE": MaximumLinesOfCode,
            "MAXIMUM_DEPTH_OF_INHERITANCE": MaximumDepthOfInheritance,
            "AVERAGE_DEPTH_OF_INHERITANCE": AverageDepthOfInheritance,
        }

        self.metrics = {name: metric_class() for name, metric_class in metrics.items()}

        for metric in self.metrics.values():
            metric.compute(self.files)

    def list(self):
        """
        List the available metrics.
        """
        return self.metrics.keys()

    def metric(self, metric_name):
        """
        Get the metric value by name.
        """
        return self.metrics[metric_name].result()

    def as_xml(self):
        """
        Return the report in XML format with all metrics.
        """
        root = ET.Element("report")

        report_time = ET.SubElement(root, "report-time")
        report_time.text = datetime.now().strftime("%d.%m.%Y")

        repo_path = ET.SubElement(root, "repository-path")
        repo_path.text = str(self.repo_path)

        metrics_elem = ET.SubElement(root, "metrics")
        for metric_name in self.metrics:
            metric_elem = ET.SubElement(metrics_elem, "metric")
            metric_elem.set("name", metric_name)
            metric_elem.text = str(format(self.metric(metric_name), ".2f"))

        ET.indent(root)
        return ET.tostring(root, encoding="unicode", method="xml")
