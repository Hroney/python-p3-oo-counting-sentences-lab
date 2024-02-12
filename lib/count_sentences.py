#!/usr/bin/env python3
import re

class MyString:

    def __init__(self, string=""):
        self._string = ""
        self.string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        if isinstance(string, str) and len(string) > 0:
            self._string = string
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.string[-1] == ".":
            return True
        else:
            return False

    def is_question(self):
        if self.string[-1] == "?":
            return True
        else:
            return False

    def is_exclamation(self):
        if self.string[-1] == "!":
            return True
        else:
            return False

    def count_sentences(self):
        value = 0
        result = re.split(r'[.?!]', self.string)
        for thing in result:
            if len(thing) > 1:
                value += 1

        return value

