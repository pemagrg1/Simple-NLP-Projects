import collections
import nltk
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

text = "Donald Trump is the worst president of USA, but Hillary is better than him"
text = text.lower()

###Normal Freq
counts = collections.Counter(text.split())
print (counts.most_common(5))

###cleaned freq
words = text.split(" ") #Replace this line
clean_text = [w for w in words if not w in stopWords]
counts = collections.Counter(" ".join(clean_text).split())
keys = counts.most_common(5)
print (keys)
