#!/usr/bin/env python3

from functools import reduce
import sys

def list_high_bits(binary_string):
    bits_low_high = [index for index,bit in enumerate(reversed(binary_string)) if int(bit)]
    return list(reversed(bits_low_high))

def get_hex_from_bits(bits):
    return reduce(lambda x,y: x + (1<<y),bits,0)

def main():
    if '-r' in sys.argv:
        bits = sorted(int(i) for i in sys.argv if i.isdecimal())
        print(get_hex_from_bits(bits))
        print(hex(get_hex_from_bits(bits)))
        print(bin(get_hex_from_bits(bits)))
    else:
        numbers = (int(arg,16) for arg in sys.argv[1:])
        binary_strings = ('{0:b}'.format(number) for number in numbers)
        high_bits = (list_high_bits(string) for string in binary_strings)
        [print(i) for i in high_bits]
    

if __name__ == '__main__':
    main()
