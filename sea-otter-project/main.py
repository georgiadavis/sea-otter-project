import jinja2
import webapp2
from twilio.rest import TwilioRestClient
import random

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())

    # Twilio API account token.
    def post(self):
        account_sid = "ACb332643db3e9450c8831d380bd722a3c"
        auth_token  = "3b80f0c5f9fc9ec030afe69149de8e49"
        client = TwilioRestClient(account_sid, auth_token)
        sender= self.request.get("sender")
        textmessage= self.request.get("textmessage")
        images=["http://unrealfacts.com/wp-content/uploads/2013/06/otters-hold-hands.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/d/d4/Sea_otter_pair2.jpg","http://www.wildnatureimages.com/images%203/080505-003.jpg","http://voices.nationalgeographic.com/files/2014/06/sea-otter-mothers-s2048x1366-p.jpg"]
        message = client.messages.create(
          to= sender,
          from_="+15712508532",
          body= textmessage,
          media_url=[random.choice(images)
            ],
          )
        print message.sid
        results = env.get_template('results.html')
        template_variables= {'sender':sender,'textmessage':textmessage}
        self.response.write(results.render(template_variables))


class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is your profile!')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/profile', ProfileHandler)
], debug=True)

