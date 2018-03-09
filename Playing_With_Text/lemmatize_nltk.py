# Lemmatize using nltk

import nltk
from nltk.stem.wordnet import WordNetLemmatizer

stemmer = WordNetLemmatizer()

text = """issues issue company companies"""
text = text.decode('utf-8')
text = text.lower()
for word in text.split():
    print word, "--->", stemmer.lemmatize(word) 
