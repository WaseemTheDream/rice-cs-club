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

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(MAIN_DIR))

NAV_BAR = [
    {'text': 'Home', 'link': 'page_index.html'},
    {'text': 'Officers', 'link': 'page_officers.html'},
    {'text': 'Sponsors', 'link': 'page_sponsors.html'},
    {'text': 'Career', 'link': 'page_career.html'},
    {'text': 'Events', 'link': 'page_events.html'},
    {'text': 'Hackathon', 'link': 'page_hackathon.html'},
    {'text': 'Contact', 'link': 'page_contact.html'}]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Requested URL: %s', self.request.path)

        # Get the page name being requested
        # assume index.html if none specified
        page_name = self.request.path
        if page_name == '/':
            page_name = NAV_BAR[0]['link']

        # Get page info
        page = JINJA_ENV.get_template(page_name).render()

        template = JINJA_ENV.get_template('template.html')
        template_vals = {'nav_bar': NAV_BAR,
                         'page_content': page}
        self.response.out.write(template.render(template_vals))

app = webapp2.WSGIApplication([('/.*', MainHandler)],
                              debug=True)
