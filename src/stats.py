"""
Module for calculating Java metrics.
"""

class JavaStats:
    """
    Class for calculating Java metrics.
    """
    def __init__(self, repo_path):
        """
        Initialize the JavaStats object.
        """
        self.repo_path = repo_path

    def list(self):
        """
        List the available metrics.
        """
        return ["NUMBER_OF_CLASSES"]

    def metric(self, metric_name):
        """
        Get the metric value by name.
        """
        return metric_name

    def as_xml(self):
        """
        Return the report in XML format.
        """
        return "<xml></xml>"
