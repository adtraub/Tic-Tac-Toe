"""
IndexHandler.py
Class for index views
"""
from Tools import pieces

from ViewHandler import Handler

class HardIndexHandler(Handler):
    """Homepage"""
    def get(self):
        self.render('index.html', **pieces)

class EasyIndexHandler(Handler):
    """Homepage"""
    def get(self):
        temp = dict(pieces)
        temp["easyMode"] = True
        self.render('index.html', **temp)
