# A simple diction based Abbreviation replacements.
'''
Date: 5-11-17
Author: Pema Gurung
'''
import nltk
import re
from nltk.corpus import indian
from nltk.tag import tnt
text="""The USA couple had been pronounced guilty by a Ghaziabad CBI court in 2013."""
sentences=nltk.tokenize.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence.strip()) for sentence in sentences]
abbrev = [
  ('USA','United States Of America'),
  ('U\.S\.A','United States Of America'),
  ('US of A', 'United States of America')
  ]
tokenized_sentences=str(tokenized_sentences).split()

#print(tokenized_sentences)
for i in tokenized_sentences:
    for j in abbrev:
        i=i.replace("'",'').replace(",",'')
        if i == j[0]:
            tokenized_sentences=str(tokenized_sentences).replace(i,j[1])
print(tokenized_sentences)
