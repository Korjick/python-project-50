from typing import Any, List

from gendiff.diff_builder import DiffNode, DiffType


def _stringify_value(value: Any) -> str:
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def _format_plain(tree: List[DiffNode], path: str) -> List[str]:
    lines: List[str] = []

    for node in tree:
        key = node['key']
        node_type = node['type']
        prop = f"{path}.{key}" if path else key

        if node_type == DiffType.NESTED:
            lines.extend(_format_plain(node['children'], prop))

        elif node_type == DiffType.ADDED:
            value = _stringify_value(node['value'])
            lines.append(
                f"Property '{prop}' was added with value: {value}"
            )

        elif node_type == DiffType.REMOVED:
            lines.append(f"Property '{prop}' was removed")

        elif node_type == DiffType.UPDATED:
            before = _stringify_value(node['value_before'])
            after = _stringify_value(node['value_after'])
            lines.append(
                f"Property '{prop}' was updated. From {before} to {after}"
            )

        elif node_type == DiffType.UNCHANGED:
            continue

    return lines


def format_plain(tree: List[DiffNode]) -> str:
    return '\n'.join(_format_plain(tree, ''))
