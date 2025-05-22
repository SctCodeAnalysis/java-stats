"""
Test the metrics.
"""

import os

from java_stats.metrics import (AverageCyclomaticComplexity,
                                AverageDepthOfInheritance, AverageLinesOfCode,
                                AverageNumberOfMethodsPerClass,
                                MaximumCyclomaticComplexity,
                                MaximumDepthOfInheritance, MaximumLinesOfCode,
                                MaximumNumberOfMethodsPerClass,
                                NumberOfClasses, NumberOfJavaFiles)
from java_stats.parser import parse_java_files


def get_test_files(repo_name):
    """Get the test files for a given repository name."""
    repo_path = os.path.join("tests", "repos", repo_name, "src")
    return parse_java_files(repo_path)


def test_simple_inheritance():
    """Test the simple inheritance metric."""
    files = get_test_files("simple_inheritance")

    avg_depth = AverageDepthOfInheritance()
    avg_depth.compute(files)
    assert avg_depth.result() == 1.5

    max_depth = MaximumDepthOfInheritance()
    max_depth.compute(files)
    assert max_depth.result() == 2


def test_complex_inheritance():
    """Test the complex inheritance metric."""
    files = get_test_files("complex_inheritance")

    avg_depth = AverageDepthOfInheritance()
    avg_depth.compute(files)
    assert avg_depth.result() == 2.0

    max_depth = MaximumDepthOfInheritance()
    max_depth.compute(files)
    assert max_depth.result() == 3


def test_complex_methods():
    """Test the complex methods metric."""
    files = get_test_files("complex_methods")

    avg_complexity = AverageCyclomaticComplexity()
    avg_complexity.compute(files)

    max_complexity = MaximumCyclomaticComplexity()
    max_complexity.compute(files)
    assert max_complexity.result() == 8


def test_many_methods():
    """Test the many methods metric."""
    files = get_test_files("many_methods")

    avg_methods = AverageNumberOfMethodsPerClass()
    avg_methods.compute(files)
    assert avg_methods.result() == 10.0

    max_methods = MaximumNumberOfMethodsPerClass()
    max_methods.compute(files)
    assert max_methods.result() == 10


def test_lines_of_code():
    """Test the lines of code metric."""
    files = get_test_files("complex_methods")

    avg_loc = AverageLinesOfCode()
    avg_loc.compute(files)
    assert avg_loc.result() > 0

    max_loc = MaximumLinesOfCode()
    max_loc.compute(files)
    assert max_loc.result() > 0


def test_file_and_class_counts():
    """Test the file and class counts metric."""
    files = get_test_files("complex_inheritance")

    num_files = NumberOfJavaFiles()
    num_files.compute(files)
    assert num_files.result() == 3

    num_classes = NumberOfClasses()
    num_classes.compute(files)
    assert num_classes.result() == 3


def test_empty_repo():
    """Test the empty repository metric."""
    files = get_test_files("empty_repo")

    metrics = [
        AverageDepthOfInheritance(),
        MaximumDepthOfInheritance(),
        AverageCyclomaticComplexity(),
        MaximumCyclomaticComplexity(),
        AverageLinesOfCode(),
        MaximumLinesOfCode(),
        AverageNumberOfMethodsPerClass(),
        MaximumNumberOfMethodsPerClass(),
        NumberOfClasses(),
        NumberOfJavaFiles(),
    ]

    for metric in metrics:
        metric.compute(files)
        assert metric.result() == 0.0
