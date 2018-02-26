import nltk
from nltk.corpus import wordnet

#in the parameter pass "n" for noun and "v" for verb
w1 = wordnet.synset('dog.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
