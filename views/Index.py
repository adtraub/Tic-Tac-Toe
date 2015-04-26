"""
Index.py
Class for index views
"""
from ViewHandler import Handler

class IndexHandler(Handler):
    """Homepage"""
    def get(self):
        self.render('index.html')
