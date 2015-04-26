"""
Adam Traub
tictacDjango

"""
import jinja2
import webapp2
from AI import AI
from Board import Board

from views.Index import IndexHandler



app = webapp2.WSGIApplication([
    ('/', IndexHandler),
], debug=True)
