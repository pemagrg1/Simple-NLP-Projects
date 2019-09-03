from nltk import word_tokenize
from nltk.tag.stanford import NERTagger
model = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
ner = '/usr/share/stanford-ner/stanford-ner.jar'
ner_model = NERTagger(model,ner)
text = """
Apple's iPhone revenue for the holiday quarter fell 15% from the same period a year ago, the company said after the markets closed Tuesday.

CEO Tim Cook blamed sales decline on a mix of factors, including a slowdown in China, foreign exchange rates, a popular battery replacement program and reduced smartphone subsidies from carriers.
"""

sentence = word_tokenize(text)
tagg_sent=ner_model.tag(sentence)
print (tagg_sent)