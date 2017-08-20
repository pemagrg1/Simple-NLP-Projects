import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

text="This is the beginning of the NER TEXT where it identifies names like John,Steve and organization like Samsung and Apple."
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    namedEnt = nltk.ne_chunk(tagged, binary=True)
    namedEnt.draw()
    
