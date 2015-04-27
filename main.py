"""
Adam Traub
tictacDjango
"""
import jinja2
import webapp2
import logging

from views.ViewHandler import Handler
from views.IndexHandler import IndexHandler
from views.AIHandler import AIHandler


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/ai', AIHandler),
], debug=True)
