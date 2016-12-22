#! coding: utf-8
from datetime import datetime

from .base import Parser, Concert


class ParserCosmonavt(Parser):
    """cosmonavt.su"""
    url = "http://cosmonavt.su"

    def get_concerts(self):
        return [
            Concert(
                artist="Metallica", datetime=datetime.now(),
                price=u"1500 рублей")
        ]
