#!/usr/bin/env python3
"""
Author : eijy <eijy@localhost>
Date   : 2022-04-26
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
from typing import NamedTuple, TextIO, List


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    out_dir: str

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--out_dir',
                        help='Outpud directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    parser.add_argument('file',
                        help='Input DNA file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))


    args = parser.parse_args()

    return Args(files=args.file, out_dir=args.out_dir)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    # create the directory if does not exist
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    # counting variables for the files
    num_files, num_seqs = 0, 0
    for fh in args.files:
        num_files += 1
        # open an output file in the output directory
        out_file = os.path.join(args.out_dir, os.path.basename(fh.name))
        print(fh.name, '->', out_file)
        out_fh = open(out_file, 'wt')

        # for each line/sequence from the input file:
            # write the transcribed sequence to the output file
            # update the number of files processed
        for dna in fh:
            num_seqs += 1
            out_fh.write(dna.rstrip().replace('T','U'))
            print(f'{dna} --> ' + dna.rstrip().replace('T', 'U'))

        out_fh.close()

    print(f'Done! Wrote {num_seqs} DNA sequence{"" if num_seqs == 1 else "s"} '
          f'into {num_files} file{"" if num_files == 1 else "s"} '
          f'located at \'{args.out_dir}\'.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
