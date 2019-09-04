"""
    Author: Pema Gurung
    Dataset:  BBC text categorization
    classes in the dataset: ['tech', 'business', 'sport', 'entertainment', 'politics']

"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from sklearn import linear_model
Project_path = "/media/ekbana/ekbana500/MY GITHUB/Machine_Learning-NLP_programs"


data = pd.read_csv('https://storage.googleapis.com/dataset-uploader/bbc/bbc-text.csv')
print (data.category.unique())
vectorizer = TfidfVectorizer(sublinear_tf=True, encoding='utf-8',
                             decode_error='ignore')


def train_test(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    print("==train test split done==")
    model = linear_model.SGDClassifier(learning_rate='constant',
                                       eta0=0.1, shuffle=False,
                                       n_iter=1)

    print("==fitting the model===")
    model.fit(X_train.A, y_train)

    print("==fit done\=")
    ypred = model.predict(X_test.A)

    print("==calculating score==")
    score = accuracy_score(y_test, ypred)
    print(score)


def train_bpsd(df, vectorizer):
    tfidf = vectorizer.fit(df["text"].values.astype('U'))

    X = vectorizer.fit_transform(df["text"].values.astype('U'))
    y = df['category']
    # train_test(X, y)
    model = svm.LinearSVC()

    print("==fitting the model===")
    model.fit(X.A, y)

    print("==fit done\=")
    return model, tfidf



model_path = Project_path + "/08. Multi-class_text_classification/models/model.pickle"
vectorizer_path = Project_path + "/08. Multi-class_text_classification/models/vectorizer.pickle"
import time
st = time.time()
model, vectorizer_model = train_bpsd(data, vectorizer)
print (time.time()-st)
pickle.dump(model, open(model_path, 'wb'))
pickle.dump(vectorizer_model, open(vectorizer_path, "wb"))

