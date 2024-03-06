#!/usr/bin/env python

from yaml import dump
import datetime
import argparse
from pathlib import Path


def make_yaml():
    return dump({
        'title':
        'New post',
        "date":
        datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
        'draft':
        True,
    })


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    yaml_header = make_yaml()
    yaml_header = '---\n' + yaml_header + '---\n\n'

    file = Path(args.path)
    assert file.parts[-1].endswith(
        'qmd'), "Input path must end with a .qmd file"
    assert not file.exists(), "File already exists."
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(yaml_header)


if __name__ == '__main__':                                                                    \

    main()
