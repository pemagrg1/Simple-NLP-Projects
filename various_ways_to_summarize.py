'''
pip install sumy
pip install gensim
==> run the code directly
'''
###LexRankSummarizer

from sumy.summarizers import luhn
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from gensim.summarization import summarize
from sumy.summarizers.luhn import LuhnSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer

LANGUAGE = "english"
SENTENCES_COUNT = 2

text = 'The contribution of cloud computing and mobile computing technologies lead to the newly emerging mobile cloud com- puting paradigm. Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources. In this paper, we focus on the third approach in supporting mobile data stream applica- tions. More specifically, we study how to optimize the com- putation partitioning of a data stream application between mobile and cloud to achieve maximum speed/throughput in processing the streaming data. To the best of our knowledge, it is the first work to study the partitioning problem for mobile data stream applica- tions, where the optimization is placed on achieving high throughput of processing the streaming data rather than minimizing the makespan of executions as in other appli- cations. We first propose a framework to provide runtime support for the dynamic computation partitioning and exe- cution of the application. Different from existing works, the framework not only allows the dynamic partitioning for a single user but also supports the sharing of computation in- stances among multiple users in the cloud to achieve efficient utilization of the underlying cloud resources. Meanwhile, the framework has better scalability because it is designed on the elastic cloud fabrics. Based on the framework, we design a genetic algorithm for optimal computation parti- tion. Both numerical evaluation and real world experiment have been performed, and the results show that the par- titioned application can achieve at least two times better performance in terms of throughput than the application without partitioning.'

parser = PlaintextParser.from_string((text), Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

def lexrank_summarizer():
    summarizer_LexRank = LexRankSummarizer(stemmer)
    summarizer_LexRank.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer_LexRank(parser.document, SENTENCES_COUNT):
        print sentence
        
def lsa_summarizer():
    summarizer_lsa = Summarizer(stemmer)
    summarizer_lsa.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer_lsa(parser.document, SENTENCES_COUNT):
        print sentence
        
def luhn_summarizer():
    summarizer_luhn = LuhnSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer_luhn(parser.document, SENTENCES_COUNT):
        print sentence
        
def gensim_summarizer():
    print (summarize(text))


lexrank_summarizer()
print "========"
lsa_summarizer()
print "========"
luhn_summarizer()
print "========"
gensim_summarizer()
