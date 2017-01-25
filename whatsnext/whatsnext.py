#! coding: utf-8
from whatsnext.parsers import ALL_PARSERS

def short_fmt(concert):
    return "{}\t{}\t{}".format(
        concert.datetime.strftime("%d %b"),
        concert.artist,
        concert.price)

if __name__ == "__main__":
    for parser in ALL_PARSERS:
        p = parser()

        for concert in p.get_concerts():
            print(p.__doc__, short_fmt(concert), sep="\t")

