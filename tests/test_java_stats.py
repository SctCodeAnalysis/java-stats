"""
Tests for the JavaStats class.
"""
from src.stats import JavaStats


def test_java_stats_initialization(repo_path):
    """
    Test that the JavaStats class initializes.
    """
    stats = JavaStats(repo_path)
    assert stats.repo_path == repo_path
