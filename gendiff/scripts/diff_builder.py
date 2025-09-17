import enum
from typing import Any, Dict, List, TypedDict


class DiffType(enum.StrEnum):
    ADDED = 'added'
    REMOVED = 'removed'
    UNCHANGED = 'unchanged'
    UPDATED = 'updated'
    NESTED = 'nested'


class DiffNode(TypedDict, total=False):
    key: str
    type: DiffType
    value: Any
    value_before: Any
    value_after: Any
    children: List['DiffNode']


def build_diff(first_data: Dict[str, Any], second_data: Dict[str, Any]) -> List[
    DiffNode]:
    keys = sorted(set(first_data.keys()) | set(second_data.keys()))
    diff: List[DiffNode] = []

    for key in keys:
        first_has = key in first_data
        second_has = key in second_data

        if first_has and second_has:
            first_value = first_data[key]
            second_value = second_data[key]

            if isinstance(first_value, dict) and isinstance(second_value, dict):
                diff.append({
                    'key': key,
                    'type': DiffType.NESTED,
                    'children': build_diff(first_value, second_value),
                })
            elif first_value == second_value:
                diff.append({
                    'key': key,
                    'type': DiffType.UNCHANGED,
                    'value': first_value,
                })
            else:
                diff.append({
                    'key': key,
                    'type': DiffType.UPDATED,
                    'value_before': first_value,
                    'value_after': second_value,
                })
        elif first_has:
            diff.append({
                'key': key,
                'type': DiffType.REMOVED,
                'value': first_data[key],
            })
        else:
            diff.append({
                'key': key,
                'type': DiffType.ADDED,
                'value': second_data[key],
            })

    return diff
