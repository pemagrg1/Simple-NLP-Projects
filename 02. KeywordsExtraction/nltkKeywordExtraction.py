import nltk
text = """
Apple's iPhone revenue for the holiday quarter fell 15% from the same period a year ago, the company said after the markets closed Tuesday.

CEO Tim Cook blamed sales decline on a mix of factors, including a slowdown in China, foreign exchange rates, a popular battery replacement program and reduced smartphone subsidies from carriers.
"""
word = nltk.word_tokenize(text)
pos_tag = nltk.pos_tag(word)
chunk = nltk.ne_chunk(pos_tag)
NE = [ " ".join(w for w, t in ele) for ele in chunk if isinstance(ele, nltk.Tree)]
print (NE)