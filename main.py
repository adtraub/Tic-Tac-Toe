"""
Adam Traub
tictacDjango
"""
import jinja2
import webapp2
import logging

from views.ViewHandler import Handler
from views.IndexHandler import HardIndexHandler, EasyIndexHandler
from views.AIHandler import HardAIHandler, EasyAIHandler


app = webapp2.WSGIApplication([
    ('/', HardIndexHandler),
    ('/easy', EasyIndexHandler),
    ('/ai', HardAIHandler),
    ('/aieasy', EasyAIHandler),
], debug=True)
