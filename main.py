"""
The Rice CS Club website. Uses Google App Engine to load some dynamic
content for a website that is mostly static.
"""

__author__ = 'Waseem Ahmad (waseem@rice.edu)'


import jinja2
import logging
import os
import webapp2

MAIN_DIR = os.path.dirname(__file__)
PAGES_DIR = os.path.join(MAIN_DIR, 'pages')

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(PAGES_DIR))

NAV_BAR = [
    {'text': 'Home', 'link': 'index'},
    {'text': 'Officers', 'link': 'officers'},
    {'text': 'Sponsors', 'link': 'sponsors'},
    {'text': 'Career', 'link': 'career'},
    {'text': 'Events', 'link': 'events'},
    {'text': 'Hack Rice', 'link': 'http://hack.rice.edu/'},
    {'text': 'Contact', 'link': 'contact'}]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Requested URL: %s', self.request.path)

        # Get the page name being requested
        # assume index.html if none specified
        page_name = self.request.path
        if page_name == '/':
            page_name = NAV_BAR[0]['link']

        # Get page info
        try:
            page = JINJA_ENV.get_template(page_name + '.html').render()
        except Exception as e:
            page = JINJA_ENV.get_template('not_found.html').render()

        template = JINJA_ENV.get_template('template.html')
        template_vals = {'nav_bar': NAV_BAR,
                         'page_content': page}
        self.response.out.write(template.render(template_vals))

app = webapp2.WSGIApplication([('/.*', MainHandler)],
                              debug=True)
