#! coding: utf-8
from datetime import datetime
import re

from .base import Parser, Concert, remove_lbr

class ParserCosmonavt(Parser):
    """Космонавт"""
    url = "http://cosmonavt.su"
    date_parse_re = re.compile("eventDate=(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
    price_parse_re = re.compile("\d+")

    def _parse_date(self, d):
        match = self.date_parse_re.search(d.strip())
        return datetime(
            day=int(match.group("day")),
            month=int(match.group("month")),
            year=int(match.group("year")))

    def _parse_price(self, p):
        p = remove_lbr(p)
        try:
            return self.price_parse_re.search(p).group(0) + "р"
        except AttributeError:
            return p

    def get_concerts(self):
        event_list = self.soup.find_all(class_="add_item concert")

        for event in event_list:
            dt = self._parse_date(str(event.find(class_="inline")))
            artist = remove_lbr(event.find(class_="add_title").find("a").text)
            price = self._parse_price(event.find(class_="add_ticket").text)

            yield Concert(artist=artist, datetime=dt, price=price)

