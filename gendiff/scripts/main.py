from gendiff.scripts.diff_builder import build_diff
from gendiff.formatters import FormatName
from gendiff.formatters.jsn import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.scripts.parser import parse_file


def generate_diff(first_file_path: str, second_file_path: str,
                  format_name: FormatName = FormatName.STYLISH) -> str:
    first_data = parse_file(first_file_path)
    second_data = parse_file(second_file_path)

    diff_tree = build_diff(first_data, second_data)

    if format_name == FormatName.STYLISH:
        return format_stylish(diff_tree)
    if format_name == FormatName.PLAIN:
        return format_plain(diff_tree)
    if format_name == FormatName.JSON:
        return format_json(diff_tree)
