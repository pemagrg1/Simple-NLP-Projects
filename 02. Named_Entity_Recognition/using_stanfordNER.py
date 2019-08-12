'''
Author: Pema Gurung
Date: 22-8-17
'''
'''
open terminal and type:
wget "http://nlp.stanford.edu/software/stanford-ner-2014-06-16.zip"
unzip stanford-ner-2014-06-16.zip
mv stanford-ner-2014-06-16 stanford-ner
sudo mv stanford-ner /usr/share/
'''
from nltk import word_tokenize
from nltk.tag.stanford import NERTagger
model = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
ner = '/usr/share/stanford-ner/stanford-ner.jar'
ner_model = NERTagger(model,ner)
sentence = word_tokenize("Hello and welcome to India I am Pema from Bangalore and I am please to help you.")
tagg_sent=ner_model.tag(sentence)
print (tagg_sent)

'''
OUTPUT:
[('Hello', 'O'), ('and', 'O'), ('welcome', 'O'), ('to', 'O'), ('India', 'LOCATION'), ('I', 'O'), ('am', 'O'), 
('Pema', 'PERSON'), ('from', 'O'), ('Bangalore', 'LOCATION'), ('and', 'O'), ('I', 'O'), ('am', 'O'), ('please', 'O'), 
('to', 'O'), ('help', 'O'), ('you', 'O'), ('.', 'O')]
'''
