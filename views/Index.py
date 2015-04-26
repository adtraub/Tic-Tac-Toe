"""
Index.py
Class for index views
"""
from ViewHandler import Handler

class IndexHandler(Handler):
    """Parent Class for homepage"""
    def get(self): 
        self.render('index.html')
