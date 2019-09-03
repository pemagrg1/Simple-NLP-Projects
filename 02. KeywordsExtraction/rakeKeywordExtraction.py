# ! pip install rake-nltk
from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
text = """
Apple's iPhone revenue for the holiday quarter fell 15% from the same period a year ago, the company said after the markets closed Tuesday.

CEO Tim Cook blamed sales decline on a mix of factors, including a slowdown in China, foreign exchange rates, a popular battery replacement program and reduced smartphone subsidies from carriers.
"""
print (r.extract_keywords_from_text(text))

print (r.get_ranked_phrases() )# To get keyword phrases ranked highest to lowest.