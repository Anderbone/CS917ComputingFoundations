"""This module should filter and sort uk phone numbers from the text file provided.
    How to use it: "python part1.py phone_log.txt" in terminal
    Author: Jiyu Yan
    Student ID: 1851015
"""
import re
from sys import argv


def inputfile(myfile):
    """ :param myfile: a file contains phone numbers in it with a '+' as a start symbol
        :return:a list contains all pure phone numbers with out any letter or symbol.
    """

    with open(myfile, 'r') as f:
        phone_num = []
        for line in f:
            num_line = ''.join(re.findall(r'[+0-9]', line)).split('+')
            del(num_line[0])  # There's a '' before every line after split('+')
            phone_num.extend(num_line)
        return phone_num


def find_uk(mylist):
    """Find and print all UK phone numbers in a specific format from a phone number lists.
    """
    new_list = []
    for i in mylist:
        if len(i) == 12 and i[:2] == '44':
            new_list.append('0'+i[2:])
    new_list.sort()
    for i in new_list:
        print(i[:5]+' '+i[5:])


if __name__ == "__main__":
    number = inputfile(argv[1])
    find_uk(number)

