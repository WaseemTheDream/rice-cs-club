"""
The Rice CS Club website. Uses Google App Engine to load some dynamic
content for a website that is mostly static.
"""

__author__ = 'Waseem Ahmad (waseem@rice.edu)'


import jinja2
import os
import webapp2


JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

NAV_BAR = [
    {'text': 'Home', 'link': 'index.html'},
    {'text': 'Officers', 'link': 'pages/officers.html'},
    {'text': 'Sponsors', 'link': 'pages/sponsors.html'},
    {'text': 'Career', 'link': 'pages/career.html'},
    {'text': 'Events', 'link': 'pages/events.html'},
    {'text': 'Hackathon', 'link': 'pages/hackathon.html'},
    {'text': 'Contact', 'link': 'pages/contact.html'}]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('index.html')
        template_vals = {'nav_bar': NAV_BAR}
        self.response.out.write(template.render(template_vals))

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
