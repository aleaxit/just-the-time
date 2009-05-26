import time
import wsgiref.handlers

from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):

  def get(self):
    fmt = self.request.get('f', '%Y-%m-%d %H:%M:%S %Z')
    fmt = fmt.replace('%t', str(time.time()))
    self.response.out.write(time.strftime(fmt)+'\n')


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
