#! coding: utf-8
from datetime import datetime
import re

from .base import Parser, Concert, remove_lbr


class ParserA2(Parser):
    """A2"""
    url = "http://a2.fm"
    date_parse_re = re.compile("(?P<day>\d{1,2})/(?P<month>\d{1,2})")
    price_parse_re = re.compile("\d+")

    def _parse_date(self, d):
        match = self.date_parse_re.search(d.strip())
        now = datetime.now()
        year = now.year

        if int(match.group("month")) < now.month:
            year = now.year + 1

        return datetime(
            day=int(match.group("day")),
            month=int(match.group("month")),
            year=year)

    def _parse_price(self, p):
        p = remove_lbr(p)
        try:
            return self.price_parse_re.search(p).group(0) + "р"
        except AttributeError:
            return p

    def get_concerts(self):
        event_list = self.soup.find(class_="css-events-list")
        for table_row in event_list.find_all("tr"):
            tds = table_row.find_all("td")

            try:
                artist = tds[2].find("a").string.strip()
                artist = remove_lbr(artist)
            except:
                artist = "PARSE ERROR"

            dt = self._parse_date(tds[0].text)

            try:
                price =tds[2].find("i").string.strip()
                price = self._parse_price(price)
            except:
                price = "PARSE ERROR"

            yield Concert(artist=artist, datetime=dt, price=price)
