import gensim
from scipy import spatial
import nltk
import numpy as np

gensim_model_path = "<path_to_gensim_model>"
"""
gensim model can be downloaded from: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
"""
model = gensim.models.KeyedVectors.load_word2vec_format(gensim_model_path, binary=True)
index2word_set = set(model.wv.index2word)


def avg_feature_vector(sentence, model, num_features, index2word_set):
    words = list(filter(None, nltk.word_tokenize(sentence)))
    feature_vec = np.zeros((num_features,), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec


def gensim_sent_sim(sent1,sent2):
    s1_afv = avg_feature_vector(sent1, model=model, num_features=300,
                                index2word_set=index2word_set)
    s2_afv = avg_feature_vector(sent2, model=model, num_features=300,
                                index2word_set=index2word_set)
    sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
    return sim


print (gensim_sent_sim("I love to eat an ice cream","I love ice cream"))
"""
score: 0.9167304039001465
"""
