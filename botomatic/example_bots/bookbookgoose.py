#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import random
from botomatic import TBot

data_file = "kindle.csv"


class BookBookGooseBot(TBot):

    def __init__(self, **kwargs):
        handle = "bookbookgoose"
        super(BookBookGooseBot, self).__init__(handle, **kwargs)

    def run(self):
        r = csv.reader(open(data_file))
        books = [row for row in r]
        random.shuffle(books)
        book = books.pop()

        book_text = book[1] + ', by ' + book[0]

        self.tweets.append(book_text[0:117] + ' ' + book[2])

        self.wrap_up()


if __name__ == '__main__':
    b = BookBookGooseBot()
