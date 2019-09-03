#Various ways to extract date from a string
#pip install dateutil,pygrok,datefinder,re,datetime,pydatum,dateparser

from dateutil import parser
from pygrok import Grok
import datefinder
import re, datetime
import nltk
from pydatum import Datum
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateparser.search import search_dates


def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

def date_finder(text):
    date =""
    date_pattern = '%{YEAR:year}-%{MONTHNUM:month}-%{MONTHDAY:day}'
    matches = list(datefinder.find_dates(s))
    match_date = re.search('\d{4}-\d{2}-\d{2}', s)

    try:
        print "====using dateutil"
        for i in s.splitlines():
            d = parser.parse(i)
            print(d.strftime("%Y-%m-%d"))
    except Exception as e:
        print e
    try:
        print "====pygrok==="
        grok = Grok(date_pattern)
        print(grok.match(s))
    except Exception as e:
        print e
    try:
        print "====using date==="
        if len(matches) > 0:
            date = matches[0]
            print date
        else:
            print 'No dates found'
    except Exception as e:
        print e
    try:
        print "====using date==="
        date = datetime.datetime.strptime(match_date.group(), '%Y-%m-%d').date()
        print date
    except Exception as e:
        print e
    try:
        print "====using Chunkgrams==="
        chunkGram = r"""NE:{<NNP>+<CD>}"""
        chunkParser = nltk.RegexpParser(chunkGram)
        sentences = nltk.sent_tokenize(text)
        tokenized_sentences = [nltk.word_tokenize(sentence.strip()) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(i) for i in tokenized_sentences]
        chunked_sentences = [chunkParser.parse(i) for i in tagged_sentences] 
        entity_names = []
        for tree in chunked_sentences:
            entity_names.extend(extract_entity_names(tree))
        print entity_names
    except Exception as e:
        print e
    try:
        print "===using pydatum=="
        datum = Datum()
        print (datum.from_iso_date_string(text))
    except Exception as e:
        print e
    try:
        print "===using dateparser=="
        date = search_dates(text.decode('ascii','ignore'))
        print date
    except Exception as e:
        print e

text = """Nov 2016
12/31/1991
 December 10, 1980
September 25, 1970
 2005-11-14
  December 1990
  October 12, 2005
  1993-06-26"""

pema_experience = """
Nitrolabs Technology Private Limited, Bangalore

“Machine Learning and Natural Language Processing Engineer” 

24July2017 – Present

"""

print date_finder(text)
print date_finder(pema_experience)
