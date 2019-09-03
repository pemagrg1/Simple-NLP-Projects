# CHUNKGRAMS


import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

text = """
Apple's iPhone revenue for the holiday quarter fell 15% from the same period a year ago, the company said after the markets closed Tuesday.

CEO Tim Cook blamed sales decline on a mix of factors, including a slowdown in China, foreign exchange rates, a popular battery replacement program and reduced smartphone subsidies from carriers.
"""
keywords = set()
sentences = nltk.sent_tokenize(text)
try:
    for i in sentences:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        #             print (tagged)
        # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
        # use pipeline "|" to use more pattern
        # use plus "+" to add more tags to the pattern
        chunkGram = r"""NE:  {<NNP>+<NNP>?|<NNP|NN>+<CC.*|NN.*>+<NNP>}
                    {<NNP>}"""
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        NE = [" ".join(w for w, t in ele) for ele in chunked if
              isinstance(ele, nltk.Tree)]
        for i in NE:
            keywords.add(i)
except Exception as e:
    print(str(e))

print(list(keywords))