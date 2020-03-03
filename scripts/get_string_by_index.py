#!/usr/bin/env python3
from pathlib import Path
import argparse


def read_string_at_index(index):
    filename = '../data/string_table_dump_decompressed'

    decompressed_table = Path(filename).read_bytes()

    s = decompressed_table[index:decompressed_table.index(b'\0', index + 1)]

    return s

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('index', type=int)
   args = parser.parse_args()


   string = read_string_at_index(args.index)

   print(string)

