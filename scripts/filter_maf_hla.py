#!/usr/bin/env python

"""
Read a directory of .maf files and .hla files, and delete the .maf files
that don't have a corresponding .hla file (and vice versa).

<this script> --maf-dir <input_dir> --hla-dir <output_dir>
"""

import argparse
from os import listdir, path

def run():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--maf-dir', required=True)
    parser.add_argument('--hla-dir', required=True)
    args = parser.parse_args()
    maf_set = set()
    for maf_filename in listdir(args.maf_dir):
        maf_set.add(maf_filename)
    for filename in listdir(args.indir):
        file_path = path.join(args.indir, filename)
        lines = [strip_info(line) for line in open(file_path)]
        new_path = path.join(args.outdir, filename)
        with open(new_path, 'a') as nf:
            output = '\n'.join(lines)
            nf.write(output)

def strip_info(line):
    line = line.strip()
    line = line.split()[0]
    line = line.split('\'')[0]
    return line

if __name__ == "__main__":
    run()

