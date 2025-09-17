from typing import Any, List

from gendiff.scripts.diff_builder import DiffNode, DiffType

INDENT_PER_LEVEL = 4
SYMBOL_INDENT_OFFSET = 2


def _stringify_value(value: Any, depth: int) -> str:
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent = _make_indent(depth + 1)
        closing_indent = _make_indent(depth)
        lines = ['{']
        for key in sorted(value.keys()):
            str_field = _stringify_value(value[key], depth + 1)
            lines.append(f"{indent}{key}: {str_field}")
        lines.append(f"{closing_indent}}}")
        return '\n'.join(lines)
    return str(value)


def _make_indent(depth: int, with_symbol: bool = False) -> str:
    base = depth * INDENT_PER_LEVEL
    shift = SYMBOL_INDENT_OFFSET if with_symbol else 0
    return ' ' * (base - shift)


def format_stylish(tree: List[DiffNode], depth: int = 0) -> str:
    lines: List[str] = ['{']
    for node in tree:
        key = node['key']
        node_type = node['type']

        if node_type == DiffType.NESTED:
            children_str = format_stylish(node['children'], depth + 1)
            lines.append(f"{_make_indent(depth + 1)}{key}: {children_str}")

        elif node_type == DiffType.UNCHANGED:
            lines.append(
                f"{_make_indent(depth + 1)}{key}: "
                f"{_stringify_value(node['value'], depth + 1)}"
            )

        elif node_type == DiffType.REMOVED:
            lines.append(
                f"{_make_indent(depth + 1, with_symbol=True)}- {key}: "
                f"{_stringify_value(node['value'], depth + 1)}"
            )

        elif node_type == DiffType.ADDED:
            lines.append(
                f"{_make_indent(depth + 1, with_symbol=True)}+ {key}: "
                f"{_stringify_value(node['value'], depth + 1)}"
            )

        elif node_type == DiffType.UPDATED:
            lines.append(
                f"{_make_indent(depth + 1, with_symbol=True)}- {key}: "
                f"{_stringify_value(node['value_before'], depth + 1)}"
            )
            lines.append(
                f"{_make_indent(depth + 1, with_symbol=True)}+ {key}: "
                f"{_stringify_value(node['value_after'], depth + 1)}"
            )

    lines.append(f"{_make_indent(depth)}}}")
    return '\n'.join(lines)
