"""
Class for parsing Java files.
"""

from dataclasses import dataclass
from pathlib import Path
import javalang


@dataclass
class ParsedFile:
    """
    Class for storing parsed files.
    """

    def __init__(self, path: Path):
        self.path = path
        self.structure = javalang.parse.parse(path.read_text())
