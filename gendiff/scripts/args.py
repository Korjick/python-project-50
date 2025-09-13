import argparse

from gendiff import generate_diff
from gendiff.formatters import FormatName


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish',
                        choices=[format_name.value
                                 for format_name in FormatName],
                        help='set format of output')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)
