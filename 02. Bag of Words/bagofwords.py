# CREATING BAG OF WORDS
import nltk
import autocorrect
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

Regexp_Tokenizer = RegexpTokenizer(r'\w+')
stopword = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()

def build_vocab(sentence_list):
    """
    1. lower
    2. remove punct
    3. stem
    4. autocorrect
    5. remove stopwords
    """
    sentences = " ".join(sentence_list)
    sentece_to_lower = sentences.lower()
    remove_punct = Regexp_Tokenizer.tokenize(sentece_to_lower)
    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in remove_punct]
    remove_stopwords = [word for word in lemmatized_word if word not in stopword]
    autocorrect_words = [autocorrect.spell(word) for word in remove_stopwords]
    vocab = list(set(autocorrect_words))
    return vocab

def sentence_vector(sentence):
    sentence_vectors = []
    sentence_tokens = nltk.word_tokenize(sentence)
    sent_vec = []
    for token in sentence_tokens:
        if token in vocab:
            sent_vec.append(1)
        else:
            sent_vec.append(0)
    sentence_vectors.append(sent_vec)
    return sentence_vectors

s1 = "It is going to rain today"
s2 = "today I am not going outside"
s3 = "I am going to watch the season premiere"
sentence_list = [s1,s2,s3]
vocab = build_vocab(sentence_list)
print(vocab)

for i in sentence_list:
    print(i,sentence_vector(i))