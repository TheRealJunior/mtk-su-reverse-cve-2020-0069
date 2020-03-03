#!/usr/bin/env python3
import argparse

class IOCTLNumber:
    def __init__(self, number):
        self.function_number = number & 0xff
        self.ascii_char = (number & 0xff00) >> 8
        self.argument_size = (number << 2) >> 15


    def __str__(self):
        return \
            f'''
            function_number={self.function_number}
            ascii_char={chr(self.ascii_char)}
            argument_size={self.argument_size}
            '''


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help='number to decode as ioctl request', type=int)
    args = parser.parse_args()

    ioctlnum = IOCTLNumber(args.num)

    print(str(ioctlnum))
