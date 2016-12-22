#!coding: utf-8
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

Concert = namedtuple("Concert", "artist datetime price")


class Parser(object):
    """Base class for all parsers, doc string is used
       as a website title"""

    url = None

    def __init__(self):
        self.data = requests.get(self.url).text
        self.soup = BeautifulSoup(self.data, "lxml")

    def get_concerts(self):
        raise NotImplementedError
