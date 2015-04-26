"""
Adam Traub
tictacDjango
"""
import jinja2
import webapp2
import logging

from views.ViewHandler import Handler
from views.Index import IndexHandler


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
], debug=True)
