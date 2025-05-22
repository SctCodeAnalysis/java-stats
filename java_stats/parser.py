"""
Parser for Java files.
"""

import os
from dataclasses import dataclass
from typing import List

import javalang


@dataclass
class ParsedFile:
    """Represents a parsed Java file."""

    path: str
    structure: javalang.tree.CompilationUnit


def parse_java_files(directory: str) -> List[ParsedFile]:
    """
    Parse all Java files in the given directory.
    """
    parsed_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    tree = javalang.parse.parse(content)
                    parsed_files.append(ParsedFile(file_path, tree))
                except (javalang.parser.JavaSyntaxError, UnicodeDecodeError) as e:
                    print(f"Error parsing {file_path}: {e}")
                    continue

    return parsed_files
