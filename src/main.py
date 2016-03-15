# -*- coding: utf-8 -*-
from bitarray import bitarray
import re
import string
import struct
from array import array
# xxd  -b file.txt


class Bitset(bitarray):
    memory = None

    def __init__(self, **arg):
        super(Bitset, self).__init__(**arg)
        self.code = {}
        if 'name' in arg.keys():
            self.name = arg['name']
        else:
            self.name = 'file.txt'

        # encode ASCII table
        for x in string.printable:
            self.code[x] = bitarray(bin(ord(x)).split('0b')[1].rjust(8, '0'))
        self.checker = re.compile(ur'([^01]+)')

    def push(self, arg):
        if (arg[0:2] == '0b') and len(arg) > 2:
            try:
                super(Bitset, self).extend(arg.split('0b')[1])
                return
            except Exception:
                pass
        a = bitarray()
        a.encode(self.code, arg)
        # arg = str(a).replace('bitarray(\'', '')
        # arg = arg.replace('\')', '')
        # super(Bitset, self).extend(arg)
        super(Bitset, self).extend(a)

    def to_file(self):
        if (len(self) % 8):
            # self.pack()
            self.fill()
        # self.memory = memoryview(self)
        bits = self.__str__()
        print ">>: ", bits, '(', len(bits), ')'
        with open(self.name, "wb") as f:
            for i in self.chunks(bits, 8):
                # int_value = int(i[::-1], base=2)
                # bin_array = struct.pack('i', int_value)
                int_value = int(i, base=2)
                bin_array = struct.pack('B', int_value)
                f.write(bin_array)

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in xrange(0, len(l), n):
            yield l[i:i + n]

    def flush(self):
        self.fill()
        self.to_file()

    def pack(self):
        size = 8 - (len(self) % 8)
        for i in range(size):
            self.insert(0, False)
        # while(len(self) % 8) > 0:
        #     self.pack()

    def __str__(self):
        output = super(Bitset, self).__str__()
        output = output.replace('bitarray(\'', '')
        output = output.replace('\')', '')
        return output


def main():
    a = Bitset()
    data = raw_input('entrada: ')
    while(len(data)):
        a.push(data)
        data = raw_input('entrada: ')

    print '<<: ', a, '(', len(a), ')'
    a.to_file()
    v = memoryview(a)
    import ipdb
    # ipdb.set_trace()
    print v.tobytes()


def test():
    pass

if __name__ == '__main__':
    main()
