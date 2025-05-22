"""
Utility functions for inheritance-related metrics.
"""

from typing import Dict, Set

import javalang

from ..parser import ParsedFile


def build_class_hierarchy(files: list[ParsedFile]) -> Dict[str, str]:
    """
    Build a dictionary mapping class names to their parent names.
    """
    class_hierarchy: Dict[str, str] = {}
    for file in files:
        try:
            tree = file.structure
            for _, class_node in tree.filter(javalang.tree.ClassDeclaration):
                class_name = class_node.name
                if class_node.extends:
                    parent_name = class_node.extends.name
                    class_hierarchy[class_name] = parent_name
                else:
                    class_hierarchy[class_name] = None
        except (javalang.parser.JavaSyntaxError, AttributeError):
            pass
    return class_hierarchy


def calculate_depth(
    class_name: str,
    hierarchy: Dict[str, str],
    visited: Set[str],
    class_depths: Dict[str, int],
) -> int:
    """
    Calculate inheritance depth for a class using DFS.
    """
    if class_name in class_depths:
        return class_depths[class_name]

    if class_name in visited:
        return 0

    visited.add(class_name)

    parent = hierarchy.get(class_name)
    if not parent:
        depth = 1
    else:
        parent_depth = calculate_depth(parent, hierarchy, visited, class_depths)
        depth = parent_depth + 1

    class_depths[class_name] = depth
    return depth


def compute_all_depths(files: list[ParsedFile]) -> Dict[str, int]:
    """
    Compute inheritance depths for all classes in the given files.
    """
    class_hierarchy = build_class_hierarchy(files)
    class_depths: Dict[str, int] = {}

    for class_name in class_hierarchy:
        if class_name not in class_depths:
            calculate_depth(class_name, class_hierarchy, set(), class_depths)

    return class_depths
