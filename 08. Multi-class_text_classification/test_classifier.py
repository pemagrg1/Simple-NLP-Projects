import pickle
import joblib


def loading_pickle(model_path):
    vectorizer = pickle.load(open(model_path+"vectorizer.pickle",'rb'))
    model = pickle.load(open(model_path+"model.pickle",'rb'))
    return vectorizer, model


def loading_joblibPickle(model_path):
    vectorizer = joblib.load(model_path+"vectorizer.sav")
    model = joblib.load(model_path+"model.sav")
    return vectorizer, model


def predict(model, vectorizer, text):
    pred = model.predict(vectorizer.transform([text]))[0]
    print("predicted class:", pred)
    return pred


if __name__ == '__main__':
    Project_path = "Machine_Learning-NLP_programs"
    model_path = Project_path + "/08. Multi-class_text_classification/models/"

    text = "tv future in the hands of viewers with home"
    # TEST using PICKLE
    vectorizer, model = loading_pickle(model_path)
    predict(model, vectorizer, text)

    #TEST using joblib
    vectorizer1, model1 = loading_joblibPickle(model_path)
    predict(model1, vectorizer1, text)