#! coding: utf-8
from datetime import datetime
import re
import json

from .base import Parser, Concert, remove_lbr


class ParserA2(Parser):
    """A2"""
    url = "http://a2.fm"

    def get_concerts(self):
        json_data = self.soup.find("div", {"data-react-class": "Affiche"})["data-react-props"]
        events = json.loads(json_data)["events"]

        for event in events:
            yield Concert(artist=event["name"],
                datetime=datetime.fromtimestamp(event["date"]),
                price=int(float(event["price"])),
                link=self.url + event["url"])