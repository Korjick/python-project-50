import os

from gendiff import generate_diff
from tests.utils import read_text


def test_generate_diff_flat_yaml():
    base_dir = os.path.join('tests', 'test_data')
    file1 = os.path.join(base_dir, 'file1.yml')
    file2 = os.path.join(base_dir, 'file2.yml')
    expected_path = os.path.join(base_dir, 'expected_flat.txt')

    expected = read_text(expected_path)
    actual = generate_diff(file1, file2)

    assert actual == expected


