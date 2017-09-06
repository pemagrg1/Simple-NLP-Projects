'''
Author: Pema Gurung
Date: 6-9-17
'''

#removing stopwords using NLTK

import nltk
from nltk.corpus import stopwords

text= "Here I am with a simple text. This, is an example to remove stopwords."
stop_words=set(stopwords.words('english'))
word_tokens=nltk.word_tokenize(text)
final_text=[i for i in word_tokens if i not in stop_words]
print (final_text)
