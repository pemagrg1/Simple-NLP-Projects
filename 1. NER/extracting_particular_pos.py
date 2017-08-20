import nltk
text="This is the beginning of the NER TEXT where it identifies names like John,Steve and organization like Samsung and Apple."
sentences = nltk.sent_tokenize(text)
tags = []

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'VBN'):
             tags.append(word)
print tags
