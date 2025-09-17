import json
from typing import Dict, List

from gendiff.scripts.diff_builder import DiffNode, DiffType


def _format_json(tree: List[DiffNode]) -> Dict[str, dict]:
    result: Dict[str, dict] = {}
    for node in tree:
        key = node['key']
        node_type = node['type']

        if node_type == DiffType.NESTED:
            result[key] = {
                'type': node_type,
                'children': _format_json(node['children']),
            }
        elif node_type == DiffType.UNCHANGED:
            result[key] = {
                'type': node_type,
                'value': node['value'],
            }
        elif node_type == DiffType.ADDED:
            result[key] = {
                'type': node_type,
                'value': node['value'],
            }
        elif node_type == DiffType.REMOVED:
            result[key] = {
                'type': node_type,
                'value': node['value'],
            }
        elif node_type == DiffType.UPDATED:
            result[key] = {
                'type': node_type,
                'value_before': node['value_before'],
                'value_after': node['value_after'],
            }
    return result


def format_json(tree: List[DiffNode]) -> str:
    mapping = _format_json(tree)
    return json.dumps(mapping, ensure_ascii=False, indent=4)
