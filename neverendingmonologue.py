import logging
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

import random
import time
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Excerpt:

    def __init__(self, file_url):
        self.file_url = file_url
        self.following = []

    def addFollowing(self, following_excerpts):
        self.following = self.following + following_excerpts

    def removeAllFollowing(self):
        self.following = []

    def getFileURL(self):
        return self.file_url

    def getFollowing(self):
        return self.following

excerpt_array = [Excerpt('audio/001-apology.wav'),
    Excerpt('audio/002-license.wav'),
    Excerpt('audio/003-classicjoke.wav'),
    Excerpt('audio/004-accent.wav'),
    Excerpt('audio/005-orderingdrinks.wav'),
    Excerpt('audio/006-indiansex.wav'),
    Excerpt('audio/007-achievable.wav'),
    Excerpt('audio/008-whyindian.wav'),
    Excerpt('audio/009-lovefuck.wav'),
    Excerpt('audio/010-drunkraces.wav'),
    Excerpt('audio/011-drunkamericans.wav'),
    Excerpt('audio/012-religiousdrinking.wav'),
    Excerpt('audio/013-whiskygenocide.wav'),
    Excerpt('audio/014-freakinheck.wav'),
    Excerpt('audio/015-operahouse.wav'),
    Excerpt('audio/016-latinwoman.wav'),
    Excerpt('audio/017-womanshapedperson.wav'),
    Excerpt('audio/018-beautifulpricks.wav'),
    Excerpt('audio/019-hypocrite.wav'),
    Excerpt('audio/020-polyester.wav'),
    Excerpt('audio/021-armani.wav'),
    Excerpt('audio/022-charlize.wav'),
    Excerpt('audio/023-oscarworthy.wav'),
    Excerpt('audio/024-telemarketers.wav'),
    Excerpt('audio/025-illegalimmigrants.wav'),
    Excerpt('audio/026-plasticsurgeon.wav'),
    Excerpt('audio/027-uglychick.wav'),
    Excerpt('audio/028-outofleague.wav'),
    Excerpt('audio/029-nonoffensive.wav'),
    Excerpt('audio/030-lowerstandards.wav'),
    Excerpt('audio/031-deodorant.wav'),
    Excerpt('audio/032-bashingneauty.wav'),
    Excerpt('audio/033-g-o-d.wav'),
    Excerpt('audio/034-idiot.wav'),
    Excerpt('audio/035-bananas.wav'),
    Excerpt('audio/036-sweatervest.wav'),
    Excerpt('audio/037-plantsbefore.wav'),
    Excerpt('audio/038-talkbananas.wav'),
    Excerpt('audio/039-forgetfreud.wav'),
    Excerpt('audio/040-godfreud.wav'),
    Excerpt('audio/041-greatestcreation.wav'),
    Excerpt('audio/042-extracredit.wav'),
    Excerpt('audio/043-fruittools.wav'),
    Excerpt('audio/044-godslurs.wav'),
    Excerpt('audio/045-lynchmob.wav'),
    Excerpt('audio/046-homophobe.wav'),
    Excerpt('audio/047-everyoneisguilty.wav'),
    Excerpt('audio/048-sogay.wav'),
    Excerpt('audio/049-confidencebooster.wav'),
    Excerpt('audio/050-spam.wav'),
    Excerpt('audio/051-twotypesofgay.wav'),
    Excerpt('audio/052-bottomtobottom.wav'),
    Excerpt('audio/053-strippermenu.wav'),
    Excerpt('audio/054-emotionallyscarred.wav'),
    Excerpt('audio/055-womenpeople.wav'),
    Excerpt('audio/056-clarinetrecital.wav'),
    Excerpt('audio/057-dentistappointment.wav'),
    Excerpt('audio/058-smalltalk.wav'),
    Excerpt('audio/059-education.wav'),
    Excerpt('audio/060-adopted.wav'),
    Excerpt('audio/061-hotnerds.wav'),
    Excerpt('audio/062-insideoutside.wav')]

START_OPTIONS = [excerpt_array[0], excerpt_array[1], excerpt_array[2],
                 excerpt_array[52], excerpt_array[45], excerpt_array[27],
                 excerpt_array[41]]

excerpt_array[0].addFollowing([excerpt_array[1], excerpt_array[8], excerpt_array[13]])
excerpt_array[1].addFollowing([excerpt_array[5], excerpt_array[2], excerpt_array[0]])
excerpt_array[2].addFollowing([excerpt_array[3], excerpt_array[4]])
excerpt_array[3].addFollowing([excerpt_array[4]])
excerpt_array[4].addFollowing([excerpt_array[9]] + START_OPTIONS)
excerpt_array[5].addFollowing([excerpt_array[6], excerpt_array[7], excerpt_array[15]])
excerpt_array[6].addFollowing([excerpt_array[7]])
excerpt_array[7].addFollowing([excerpt_array[15]])
excerpt_array[8].addFollowing([excerpt_array[13], excerpt_array[14]])
excerpt_array[9].addFollowing([excerpt_array[10], excerpt_array[11]])
excerpt_array[10].addFollowing([excerpt_array[11]])
excerpt_array[11].addFollowing([excerpt_array[12]] + START_OPTIONS)
excerpt_array[12].addFollowing(START_OPTIONS)
excerpt_array[13].addFollowing([excerpt_array[32]])
excerpt_array[14].addFollowing([excerpt_array[28], excerpt_array[44]])
excerpt_array[15].addFollowing([excerpt_array[16], excerpt_array[17]])
excerpt_array[16].addFollowing([excerpt_array[17]])
excerpt_array[17].addFollowing([excerpt_array[18]])
excerpt_array[18].addFollowing([excerpt_array[19], excerpt_array[23], excerpt_array[24]])
excerpt_array[19].addFollowing([excerpt_array[20], excerpt_array[21]])
excerpt_array[20].addFollowing([excerpt_array[21]])
excerpt_array[21].addFollowing([excerpt_array[22], excerpt_array[23]])
excerpt_array[22].addFollowing([excerpt_array[23], excerpt_array[24]])
excerpt_array[23].addFollowing([excerpt_array[24], excerpt_array[26]])
excerpt_array[24].addFollowing([excerpt_array[25], excerpt_array[26]])
excerpt_array[25].addFollowing([excerpt_array[26]])
excerpt_array[26].addFollowing([excerpt_array[27]])
excerpt_array[27].addFollowing([excerpt_array[29]])
excerpt_array[28].addFollowing([excerpt_array[32]])
excerpt_array[29].addFollowing([excerpt_array[30]])
excerpt_array[30].addFollowing(START_OPTIONS)
excerpt_array[31].addFollowing(START_OPTIONS)
excerpt_array[32].addFollowing([excerpt_array[33], excerpt_array[43]])
excerpt_array[33].addFollowing([excerpt_array[34], excerpt_array[43]])
excerpt_array[34].addFollowing([excerpt_array[35], excerpt_array[36]])
excerpt_array[35].addFollowing([excerpt_array[36]])
excerpt_array[36].addFollowing([excerpt_array[37], excerpt_array[38], excerpt_array[42]])
excerpt_array[37].addFollowing([excerpt_array[38], excerpt_array[42]])
excerpt_array[38].addFollowing([excerpt_array[39], excerpt_array[40]])
excerpt_array[39].addFollowing([excerpt_array[40]])
excerpt_array[40].addFollowing([excerpt_array[41]])
excerpt_array[41].addFollowing(START_OPTIONS)
excerpt_array[42].addFollowing([excerpt_array[41]])
excerpt_array[43].addFollowing([excerpt_array[44]])
excerpt_array[44].addFollowing([excerpt_array[46]])
excerpt_array[45].addFollowing([excerpt_array[46], excerpt_array[49]])
excerpt_array[46].addFollowing([excerpt_array[45], excerpt_array[48], excerpt_array[50], excerpt_array[61]])
excerpt_array[47].addFollowing([excerpt_array[48], excerpt_array[50], excerpt_array[61]])
excerpt_array[48].addFollowing([excerpt_array[49]])
excerpt_array[49].addFollowing([excerpt_array[50]])
excerpt_array[50].addFollowing([excerpt_array[51]])
excerpt_array[51].addFollowing(START_OPTIONS)
excerpt_array[52].addFollowing([excerpt_array[53], excerpt_array[54]])
excerpt_array[53].addFollowing([excerpt_array[54]])
excerpt_array[54].addFollowing([excerpt_array[55], excerpt_array[56]])
excerpt_array[55].addFollowing([excerpt_array[56]])
excerpt_array[56].addFollowing([excerpt_array[57]])
excerpt_array[57].addFollowing([excerpt_array[58], excerpt_array[59]])
excerpt_array[58].addFollowing([excerpt_array[59]] + START_OPTIONS)
excerpt_array[59].addFollowing(START_OPTIONS)
excerpt_array[61].addFollowing([excerpt_array[51]])

current_excerpt = 'start'

listened_set = set([])

def audioKey(audio_url):
    """Constructs a Datastore key for the url for an audio file, audio_url."""
    return ndb.Key('AudioUrl', audio_url)

def aggregateKey():
    """Constructs a Datastore key for the aggregated excerpt data"""
    return ndb.Key('AggKey', '1')

class Session(ndb.Model):
    """Models an individual listening session entry."""
    listener = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    laugh_array = ndb.TextProperty()

class Aggregate(ndb.Model):
    """Models aggregated data over an audio excerpt."""
    audio_url = ndb.StringProperty()
    total_laughs = ndb.TextProperty()
    total_listens = ndb.IntegerProperty(indexed=False)


class MainPage(webapp2.RequestHandler):


    def get(self):

        global current_excerpt
        current_excerpt = START_OPTIONS[random.randint(0, len(START_OPTIONS) - 1)]
        
        aggregate = Aggregate.get_by_id(current_excerpt.getFileURL(), parent = aggregateKey())
        logging.debug(str(aggregate))

        if aggregate is None or aggregate.total_listens is None:
            total_listens = 0
        else:
            total_listens = aggregate.total_listens
        if aggregate is None or aggregate.total_laughs is None:
            total_laughs = ''
        else:
            total_laughs = aggregate.total_laughs

        template_values = {
            'audio_url': current_excerpt.getFileURL(),
            'total_laughs': total_laughs,
            'total_listens': total_listens,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class AudioLoader(webapp2.RequestHandler):

    def get(self):

        global current_excerpt
        global listened_set

        listened_set.add(current_excerpt)
        following_excerpts_set = set(current_excerpt.getFollowing())
        diff_excerpts = following_excerpts_set.difference(listened_set)
        if len(diff_excerpts) == 0:
            next_excerpts = current_excerpt.getFollowing()
        else:
            next_excerpts = list(diff_excerpts)
        current_excerpt = next_excerpts[random.randint(0, len(next_excerpts) - 1)]

        aggregate = Aggregate.get_by_id(current_excerpt.getFileURL(), parent = aggregateKey())
        logging.debug(str(aggregate))

        if aggregate is None or aggregate.total_listens is None:
            total_listens = 0
        else:
            total_listens = aggregate.total_listens
        if aggregate is None or aggregate.total_laughs is None:
            total_laughs = ''
        else:
            total_laughs = aggregate.total_laughs

        template_values = {
            'audio_url': current_excerpt.getFileURL(),
            'total_laughs': total_laughs,
            'total_listens': total_listens,
        }

        logging.info(str(template_values))

        self.response.write(json.dumps(template_values))


class Aggregator(webapp2.RequestHandler):

    def get(self):
       
        global excerpt_array

        start = time.time()
        session_count = 0

        for excerpt in excerpt_array:
            excerpt_query = Session.query(ancestor = audioKey(excerpt.getFileURL()))
            total_laughs = []
            total_listens = 0
            for session in excerpt_query:
                if session.laugh_array is not None:
                    laugh_str = session.laugh_array.split(',')
                    laugh_array = [int(laugh) for laugh in laugh_str]
                else:
                    laugh_array = []
                if len(laugh_array) > len(total_laughs):
                    total_laughs += ([0]*(len(laugh_array) - len(total_laughs)))
                for i in range(len(laugh_array)):
                    total_laughs[i] += laugh_array[i]
                total_listens += 1
                session_count += 1
            aggregate = Aggregate(parent = aggregateKey(), id = excerpt.getFileURL())
            aggregate.audio_url = excerpt.getFileURL()
            aggregate.total_laughs = str(total_laughs).strip('[]')
            aggregate.total_listens = total_listens
            key = aggregate.put()
            logging.debug('Added aggregation: ' + str(key))
        end = time.time()

        template_values = {
            'elapsed_time': end - start,
            'excerpt_num': len(excerpt_array),
            'session_count': session_count,
        }
        template = JINJA_ENVIRONMENT.get_template('aggregate.html')
        self.response.write(template.render(template_values))

class SessionLogger(webapp2.RequestHandler):

    def post(self):

        session_data = json.loads(self.request.get('json'))
        logging.info(str(session_data))
        session = Session(parent = audioKey(session_data['audio_url']))
        session.laugh_array = str(session_data['laugh_array']).strip('[]')
        if users.get_current_user():
            session.listener = users.get_current_user()
        key = session.put()
        logging.info('Added session: ' + str(key))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/audioloader', AudioLoader),
    ('/aggregate', Aggregator),
    ('/logsession', SessionLogger)
], debug=True)