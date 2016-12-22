#! coding: utf-8
from datetime import datetime

from .base import Parser, Concert


class ParserA2(Parser):
    """a2.fm"""
    url = "http://a2.fm"

    def get_concerts(self):
        return [
            Concert(
                artist="Arctic Monkeys", datetime=datetime.now(),
                price=u"1500 рублей")
        ]
