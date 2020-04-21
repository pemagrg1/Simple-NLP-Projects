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
from keras.models import Sequential
from keras import layers


output_dict = {
    "tech":0,
    "business":1,
    "sport":2,
    "entertainment":3,
    "politics":4,
}


def get_label(text):
    return output_dict[text]


def train_model(df, vectorizer):
    tfidf = vectorizer.fit(df["text"].values.astype('U'))

    X = vectorizer.fit_transform(df["text"].values.astype('U'))
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    input_dim = X_train.shape[1]  # Number of features

    model = Sequential()
    model.add(layers.Dense(10, input_dim=input_dim, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

    # train_test(X, y,model)

    print("==fitting the model===")
    model.fit(X_train.A, y_train,
                epochs = 50,
                verbose = True,
                validation_data = (X_test.A, y_test),
                batch_size = 10)

    print("==fit done\=")
    loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
    print("Training Accuracy: {:.4f}".format(accuracy))
    loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
    print("Testing Accuracy:  {:.4f}".format(accuracy))
    return model, tfidf


Project_path = "Machine_Learning-NLP_programs"
data = pd.read_csv('https://storage.googleapis.com/dataset-uploader/bbc/bbc-text.csv')
print (data.category.unique())

data["label"] = data["category"].apply(get_label)

vectorizer = TfidfVectorizer(sublinear_tf=True, encoding='utf-8',
                             decode_error='ignore')
model, vectorizer_model = train_model(data, vectorizer)


