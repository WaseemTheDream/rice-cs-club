"""
The Rice CS Club website. Uses Google App Engine to load some dynamic
content for a website that is mostly static.
"""

__author__ = 'Waseem Ahmad (waseem@rice.edu)'


import jinja2
import json
import logging
import os
import webapp2

MAIN_DIR = os.path.dirname(__file__)
PAGES_DIR = os.path.join(MAIN_DIR, 'pages')

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(PAGES_DIR))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        global_data = json.loads(open('global.json', 'r').read())

        # Get the page name being requested
        # assume index.html if none specified
        page_name = self.request.path
        if page_name == '/':
            page_name = global_data['nav_bar'][0]['link']

        # Get page info
        try:
            page = JINJA_ENV.get_template(page_name + '.html')
        except jinja2.TemplateNotFound as e:
            page = JINJA_ENV.get_template('not_found.html')

        self.response.out.write(page.render(global_data))

app = webapp2.WSGIApplication([('/.*', MainHandler)],
                              debug=True)
