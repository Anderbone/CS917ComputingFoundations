"""This module should filter and sort uk phone numbers from the text file provided. """
import re
from sys import argv


def find_uk_num(myfile):
    with open(myfile, 'r') as f:
        phone_num = []
        uk_num = []
        for line in f:
            num_line = ''.join(re.findall(r'[+0-9]', line)).split('+')
            del(num_line[0])  # There's a '' before every line after split('+')
            phone_num.extend(num_line)
        for i in phone_num:
            if len(i) == 12 and i[:2] == '44':
                uk_num.append('0' + i[2:])
        return uk_num


if __name__ == "__main__":
    # a = inputfile('small_log.txt')
    b = find_uk_num('small_log.txt')
    b.sort()
    for i in b:
        print(i[:5]+' '+i[5:])

