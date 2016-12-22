#! coding: utf-8
from parsers import ALL_PARSERS

for parser in ALL_PARSERS:
    p = parser()

    for concert in p.get_concerts():
        print("{}\t{}\t{}\t{}".format(p.__doc__, *concert))
