#Tools.py
import webapp2
import jinja2
import os
import urllib2

#directories
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

#jinja
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
