from textblob import TextBlob

text = """
Apple's iPhone revenue for the holiday quarter fell 15% from the same period a year ago, the company said after the markets closed Tuesday.

CEO Tim Cook blamed sales decline on a mix of factors, including a slowdown in China, foreign exchange rates, a popular battery replacement program and reduced smartphone subsidies from carriers.
"""
blob = TextBlob(text)
# print (blob.tags )          # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

print (blob.noun_phrases)   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)
# 0.060
# -0.341

# print (blob.translate(to="es"))  # 'La amenaza titular de The Blob...'