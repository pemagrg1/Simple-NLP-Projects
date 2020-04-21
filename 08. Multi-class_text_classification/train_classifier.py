"""
    Author: Pema Gurung
    Dataset:  BBC text categorization
    classes in the dataset: ['tech', 'business', 'sport', 'entertainment', 'politics']

"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

import pickle
import joblib

data = pd.read_csv('https://storage.googleapis.com/dataset-uploader/bbc/bbc-text.csv')
print (data.category.unique())
print(data.head(2))

def save_pkl_joblib(model_path):
    joblib.dump(model, model_path+"model.sav")
    joblib.dump(vectorizer_model, model_path+"vectorizer.sav")
    print ("====done saving into pickle using Joblib!====")


def save_pkl_pickle(model_path):
    pickle.dump(model, open(model_path+"model.pickle", 'wb'))
    pickle.dump(vectorizer_model, open(model_path+"vectorizer.pickle", "wb"))
    print ("====done saving into pickle using Pickle!====")


def train_test_model(X, y):
    #Vectorizer
    vectorizer_model = TfidfVectorizer(stop_words='english')
    X = vectorizer_model.fit_transform(X.values.astype('U'))
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # MODEL Training
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    print(model.score(X_test, y_test))

    return model, vectorizer_model

Project_path = "Machine_Learning-NLP_programs"
model_path = Project_path + "/08. Multi-class_text_classification/models/"

model, vectorizer_model = train_test_model(data["text"], data["category"])
save_pkl_pickle(model_path)
save_pkl_joblib(model_path)
