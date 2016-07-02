# -*- coding: utf-8 -*-
from bitarray import bitarray
import re
import string
import struct
from bitargs import _parser
# xxd  -b file.txt


class Bitset(bitarray):
    memory = None

    def __init__(self, name='file.bin', verbose=True):
        super(Bitset, self).__init__()
        self.code = {}
        self.verbose = verbose
        self.name = name

        # encode ASCII table
        for x in string.printable:
            self.code[x] = bitarray(bin(ord(x)).split('0b')[1].rjust(8, '0'))
        # self.checker = re.compile(ur'([^01]+)')

    def push(self, arg):
        if type(arg) == int:
            if arg < 0:
                arg = (1 << 8) + arg
            arg = '{:b}'.format(arg)
        elif type(arg) != str:
            raise Exception('Format not supported')

        super(Bitset, self).extend(arg)

    def to_file(self):
        if (len(self) % 8):
            # self.pack()
            self.fill()
        bits = self.__str__()
        if self.verbose:
            print(">>: ", bits, '(', len(bits), ')')
        with open(self.name, "wb") as f:
            for i in self.chunks(bits, 8):
                # int_value = int(i[::-1], base=2)
                # bin_array = struct.pack('i', int_value)
                int_value = int(i, base=2)
                bin_array = struct.pack('B', int_value)
                f.write(bin_array)

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def flush(self):
        self.fill()
        self.memory = memoryview(self)

    def pack(self):
        size = 8 - (len(self) % 8)
        for i in range(size):
            self.insert(0, False)

    def __str__(self):
        output = super(Bitset, self).__str__()
        output = output.replace('bitarray(\'', '')
        output = output.replace('\')', '')
        return output


def main():

    (_options, _args) = _parser.parse_args()
    a = Bitset()
    a.name = _options.filename
    a.verbose = _options.verbose
    if not _args:
        _parser.print_help()
        return
    result = re.findall('[^10]', _args[0])
    if len(result) != 0:
        _args[0] = int(_args[0])
    a.push(_args[0])

    if _options.verbose:
        print('<<: ', a, '(', len(a), ')')
    a.to_file()


def test():
    pass

if __name__ == '__main__':
    main()
