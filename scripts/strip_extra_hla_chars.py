#!/usr/bin/env python

"""
Strip extra characters from the filenames of HLA files.

<this script> --num-chars <num_chars> --hla-dir <input_dir>
"""

import argparse
from os import listdir, path, rename, extsep

def run():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--hla-dir', required=True)
    parser.add_argument('--num-chars', required=True)
    args = parser.parse_args()
    for filename in listdir(args.hla_dir):
        basename, ext = path.splitext(filename)
        if ext == '.hla':
            file_path = path.join(args.hla_dir, filename)
            new_filename = basename[:int(args.num_chars)]
            rename(file_path, path.join(args.hla_dir,
                new_filename + ext))

if __name__ == "__main__":
    run()
