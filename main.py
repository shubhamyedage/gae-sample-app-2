import webapp2

class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world!")

app = webapp2.WSGIApplication([
    ('/', HomePage)
])
