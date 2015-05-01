"""
IndexHandler.py
Class for index views
"""
from Tools import pieces

from ViewHandler import Handler

class IndexHandler(Handler):
    """Homepage"""
    def get(self):
        self.render('index.html', **pieces)
