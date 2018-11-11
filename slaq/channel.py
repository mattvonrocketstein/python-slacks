""" slaq.channel
"""

from loggable import Loggable


class Channel(Loggable):
    def __init__(self, **data):
        self.data = data

    def __str__(self):
        return self.data['name']

    def __repr__(self):
        return '<Channel #{}>'.format(str(self))

    def __getattr__(self, name):
        return getattr(self, 'data')[name]
