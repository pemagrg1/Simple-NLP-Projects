'''
Author: Pema Gurung
Date: 29-8-17
'''
#custumise your chunks by defining the pattern
import nltk
from nltk import word_tokenize,pos_tag,ne_chunk
text="Merck & Co said on Monday that its Keytruda immunotherapy failed to extend survival in previously treated patients \
with advanced head and neck cancer more than the standard combination therapy in a late-stage trial. The drug,\
which blocks a mechanism tumors use to hide from the immune system allowing it to recognize and attack the cancer, \
won accelerated US approval last August for these patients based on its ability to shrink tumors. As a condition of \
the accelerated approval, Merck was required to conduct a trial to demonstrate superiority over standard treatment \
and verify the clinical benefit of Keytruda in this patient population."

def NERprocess():
    sentences = nltk.sent_tokenize(text)
    try:
        for i in sentences:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            #use pipeline "|" to use more pattern
            #use plus "+" to add more tags to the pattern 
            chunkGram = r"""NE:  {<NN>+<NN>?|<NNP|NN>+<CC.*>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #print (chunked)
            chunked.draw()
    except Exception as e:
        print(str(e))
        
entities = NERprocess()

'''
chunk: Merck NNP
chunk: Keytruda NNP immunotherapy NN
'''
