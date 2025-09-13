import os

from gendiff import generate_diff
from tests.utils import read_text


def test_generate_diff_nested_json():
    base_dir = os.path.join('tests', 'test_data')
    file1 = os.path.join(base_dir, 'nested_file1.json')
    file2 = os.path.join(base_dir, 'nested_file2.json')
    expected_path = os.path.join(base_dir, 'expected_nested_stylish.txt')

    expected = read_text(expected_path)
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_generate_diff_nested_yaml():
    base_dir = os.path.join('tests', 'test_data')
    file1 = os.path.join(base_dir, 'nested_file1.yml')
    file2 = os.path.join(base_dir, 'nested_file2.yml')
    expected_path = os.path.join(base_dir, 'expected_nested_stylish.txt')

    expected = read_text(expected_path)
    actual = generate_diff(file1, file2)
    assert actual == expected


