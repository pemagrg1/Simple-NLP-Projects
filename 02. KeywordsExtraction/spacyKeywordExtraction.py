import spacy
nlp = spacy.load("en")
text = """
Apple's iPhone revenue for the holiday quarter fell 15% from the same period a year ago, the company said after the markets closed Tuesday.

CEO Tim Cook blamed sales decline on a mix of factors, including a slowdown in China, foreign exchange rates, a popular battery replacement program and reduced smartphone subsidies from carriers.
"""
text = nlp(text)
labels = set([w.label_ for w in text.ents])
for label in labels:
    entities = [e.string for e in text.ents if label==e.label_]
    entities = list(set(entities))
    print((entities))