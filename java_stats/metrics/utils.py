"""
Utility functions for metrics calculations.
"""

from pathlib import Path
from typing import Any, Callable, List

import javalang

from ..parser import ParsedFile


def calculate_cyclomatic_complexity(method: javalang.tree.MethodDeclaration) -> int:
    """
    Calculate the cyclomatic complexity of a method.
    """
    complexity = 1

    if_count = len(list(method.filter(javalang.tree.IfStatement)))
    complexity += if_count

    for_count = len(list(method.filter(javalang.tree.ForStatement)))
    complexity += for_count

    while_count = len(list(method.filter(javalang.tree.WhileStatement)))
    complexity += while_count

    do_count = len(list(method.filter(javalang.tree.DoStatement)))
    complexity += do_count

    catch_count = len(list(method.filter(javalang.tree.CatchClause)))
    complexity += catch_count

    switch_cases = 0
    for _, node in method.filter(javalang.tree.SwitchStatement):
        switch_cases += len(node.cases)
    complexity += switch_cases

    logical_ops = 0
    for _, node in method.filter(javalang.tree.BinaryOperation):
        if node.operator in ("&&", "||"):
            logical_ops += 1
    complexity += logical_ops

    return complexity


def count_method_lines(file: ParsedFile, method_node) -> int:
    """
    Count the number of lines in a method.
    """
    try:
        content = Path(file.path).read_text(encoding="utf-8")
        lines = content.splitlines()

        start_line = method_node.position.line
        end_line = method_node.position.line

        brace_stack = 0
        for i in range(start_line - 1, len(lines)):
            line = lines[i]
            brace_stack += line.count("{")
            brace_stack -= line.count("}")
            if brace_stack == 0 and i > start_line - 1:
                end_line = i + 1
                break

        return end_line - start_line + 1
    except (AttributeError, IndexError):
        return 0


def count_class_lines(file: ParsedFile, class_node) -> int:
    """
    Count the number of lines in a class.
    """
    try:
        content = Path(file.path).read_text(encoding="utf-8")
        lines = content.splitlines()

        start_line = class_node.position.line
        end_line = class_node.position.line

        brace_stack = 0
        for i in range(start_line - 1, len(lines)):
            line = lines[i]
            brace_stack += line.count("{")
            brace_stack -= line.count("}")
            if brace_stack == 0 and i > start_line - 1:
                end_line = i + 1
                break

        return end_line - start_line + 1
    except (AttributeError, IndexError):
        return 0


def process_java_files(
    files: List[ParsedFile],
    process_method: Callable[[javalang.tree.MethodDeclaration], Any],
) -> None:
    """
    Process Java files and their methods.
    """
    for file in files:
        tree = file.structure
        class_count = 0
        method_count = 0
        for _, class_node in tree.filter(javalang.tree.ClassDeclaration):
            class_count += 1
            for method in class_node.methods:
                method_count += 1
                process_method(method)
