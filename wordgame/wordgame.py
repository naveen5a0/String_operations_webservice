# [START imports]
import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import memcache
import json
import difflib
import json as m_json
import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'



class Greeting(ndb.Model):
    """Models a Guestbook entry with an author, content, avatar, and date."""
    input_data = ndb.StringProperty()
    operation = ndb.TextProperty()
    output_data = ndb.StringProperty()



def guestbook_key(guestbook_name=None):
    """Constructs a Datastore key for a Guestbook entity with name."""
    return ndb.Key('Guestbook', guestbook_name or 'default_guestbook')


class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            template = JINJA_ENVIRONMENT.get_template('contact.html')
            greetings = Greeting.query().fetch(10)
            pros_info_arr = []
            for greeting in greetings:
                pros_info_arr.append(greeting.input_data)

            template_values = {
                'pros_arr': pros_info_arr,
                'nickname':nickname,
                'logout_url':logout_url,

            }
            self.response.write(template.render(template_values))

        else:
            greeting = ('Welcome to word processing system <br> <a href="%s">Sign in with your google account</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)
#prev code
    '''
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        greetings = Greeting.query().fetch(10)
        pros_info_arr = []
        for greeting in greetings:
            pros_info_arr.append(greeting.input_data)

        template_values = {
            'pros': pros_info_arr,
        }
        self.response.write(template.render(template_values))
'''


class Guestbook(webapp2.RequestHandler):

    def post(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        count = memcache.get('count')
        if (count== None):
            memcache.set('count',1)
        else:
            memcache.set('count',count+1)

        info = self.request.get('feedback')
        selection = self.request.get('pref')
        greeting = Greeting(parent=guestbook_key('browse'))
        greeting.input_data = info
        greeting.put()
        if(selection == 'browse'):
            pros_info = browse(info)
        elif(selection == 'palindrome'):
            pros_info = palindrome(info)
        elif(selection == 'reverse'):
            pros_info = reverse(info)
        elif(selection == 'count'):
            pros_info = countword(info)
        elif(selection == 'sort'):
            pros_info = sort(info)
        elif(selection == 'digit'):
            pros_info = digit(info)
        elif(selection == 'compare'):
            info2 = self.request.get('feedback2')
            pros_info = compare(info,info2)
        elif(selection == 'merge'):
            info2 = self.request.get('feedback2')
            pros_info = merge(info,info2)
        greetings = Greeting.query().fetch(10)
        pros_info_arr = []
        for greeting in greetings:
            pros_info_arr.append(greeting.input_data)
        template_values = {
            'pros_arr':pros_info_arr,
            'pros': pros_info,
            'count':count,
            'nickname':nickname,
            'logout_url':logout_url,
        }
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render(template_values))

def palindrome(input_key):
     
    c=0;
    palin_dict = {}
    palin_array = []
    para_array=input_key.split(" ")
    for k in para_array:
        if(k==k[::-1]):
            print k
            palin_array.append(k)
            c=c+1

    
    return palin_array
def reverse(input_key):
     
    return input_key[::-1]

def merge(input_key,input_key2):
     
    
    return input_key+input_key2
def compare(input_key,input_key2):
    para1 = input_key
    para2 = input_key2
    difflines_array = []
    compare_dict = {}
    para1lines = para1.splitlines(1)
    para2lines = para2.splitlines(1)
    diffInstance = difflib.Differ()
    diffList = list(diffInstance.compare(para1lines, para2lines))
    print '-'*50
    for line in diffList:
      if line[0] == '-':
        difflines_array.append(line)
        difflines_count = len(difflines_array)
    compare_dict["para1"]=para1
    compare_dict["para2"]=para2
    compare_dict["count"] = difflines_count
    compare_dict["differentlines"] = difflines_array     

    return compare_dict

def digit(input_key):
    digit_dict = []
    for k in input_key:
        if k.isdigit():
            digit_dict.append(k)
    return digit_dict

def sort(input_key):
    sort_dict = {}
    for k in input_key.split():
        sort_dict.setdefault(len(k),[]).append(k)
    print sort_dict
    return sort_dict

def countword(input_key):
    c=0
    para_dict={}
    word_dict2={}
    para_array1=[]
    word_length=[]
    para_array=input_key.split(" ")
    for k in para_array:
        para_array1.append(k)
        p=len(k)
        word_dict2[k]=p
        c=c+p
    para_dict['count_letters_excluding_spaces']=c
    para_dict['each_word_count']=word_dict2
    return para_dict

def browse(input_key):

    input_key1 = urllib.urlencode ( { 'q' : input_key } )
    raw_result = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + input_key1 ).read()
    json = m_json.loads ( raw_result )
    results = json [ 'responseData' ] [ 'results' ]
    title_array = []
    result_dict = {}
    for result in results:
        title = result['url']
        print title
        title_array.append(title)
    result_dict["count"]=len(title_array)
    result_dict["search_pattern"]=input_key
    result_dict["urls"]=title_array
    return result_dict

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
