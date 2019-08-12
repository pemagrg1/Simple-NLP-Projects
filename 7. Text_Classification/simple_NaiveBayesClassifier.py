'''
Author: Pema Gurung
Date: 21-9-17
Prog: Simple Naive Bayes Classifier using TextBlob.
'''
train=[
    ('Apple','fruits'),
    ('Mango','fruits'),
    ('Onion','vegetables'),
    ('Spinach','vegetables'),
    ('Potato','vegetables'),
    ('Cabbage','vegetables'),
    ('Banana','fruits'),
    ('Watermelon','fruits'),
    ('Raddish','vegetables')
    ]

from textblob.classifiers import NaiveBayesClassifier
model=NaiveBayesClassifier(train)
predict=model.classify("Banana")
print(predict)
