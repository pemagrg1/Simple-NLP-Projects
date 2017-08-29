'''
Author: Pema Gurung
Date: 20-8-17
'''

import nltk
text="This is a demo for NER TEXT where it identifies names like John,Steve and organization like Samsung and Apple and extracts only Noun, Proper Noun, Verb noun and Singular Noun"
sentences = nltk.sent_tokenize(text)
tags = []

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'VBN'):
             tags.append(word)
print (tags)
