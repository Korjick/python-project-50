import json
import os

from gendiff import generate_diff
from gendiff.formatters import FormatName
from tests.utils import read_text


def test_generate_diff_json_matches_expected_mapping_structure():
    base_dir = os.path.join('tests', 'test_data')
    file1 = os.path.join(base_dir, 'nested_file1.json')
    file2 = os.path.join(base_dir, 'nested_file2.json')
    expected_path = os.path.join(base_dir, 'expected_json.txt')

    output = generate_diff(file1, file2, FormatName.JSON)
    expected = read_text(expected_path)

    assert json.loads(output) == json.loads(expected)
