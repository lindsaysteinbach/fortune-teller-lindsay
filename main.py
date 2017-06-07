#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I am the main handler')

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortune_page = JINJA_ENVIRONMENT.get_template("templates/fortune.html")
        user_name = "Lindsay"
        user_location = "Boston"
        self.response.write(fortune_page.render(
        {"input_name" : user_name,
        "input_location" : user_location}
        ))

class CountHandler(webapp2.RequestHandler):
    def get(self):
        count_page = JINJA_ENVIRONMENT.get_template("templates/number-start.html")
        self.response.write(count_page.render())

    def post(self):
        banana = JINJA_ENVIRONMENT.get_template("templates/count.html")
        users_fav_num = 27
        self.response.write(banana.render(
        {"user_num" : users_fav_num}
        ))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/fortune', FortuneHandler)
], debug=True)
