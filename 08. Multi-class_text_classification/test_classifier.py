import pickle

Project_path = "/media/ekbana/ekbana500/MY GITHUB/Machine_Learning-NLP_programs"
model_path = Project_path + "/08. Multi-class_text_classification/models/model.pickle"
vectorizer_path = Project_path + "/08. Multi-class_text_classification/models/vectorizer.pickle"

vectorizer = pickle.load(open(vectorizer_path,'rb'))
model = pickle.load(open(model_path,'rb'))
pred = model.predict(vectorizer.transform(["i have got a new phone. its from Apple.. and i love it!"]))[0]
print ("predicted class:", pred)
