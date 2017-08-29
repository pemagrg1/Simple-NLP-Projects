'''
Author: Pema Gurung
Date: 30-8-17
'''
#Simple Regular Expression Based NP Chunker
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
            return tagged
    except Exception as e:
        print(str(e))

entities = NERprocess()
print (entities)
sentence=entities
grammar = "NP######:{<DT>?<JJ>*<NN>}"
cp=nltk.RegexpParser(grammar)
result=cp.parse(sentence)
print (result)
'''
(S
  Merck/NNP
  &/CC
  Co/NNP
  said/VBD
  on/IN
  Monday/NNP
  that/IN
  its/PRP$
  Keytruda/NNP
  (NP###### immunotherapy/NN)
  failed/VBD
  to/TO
  extend/VB
  (NP###### survival/NN)
  in/IN
  previously/RB
  treated/VBN
  patients/NNS
  with/IN
  (NP###### advanced/JJ head/NN)
  and/CC
  (NP###### neck/NN)
  (NP###### cancer/NN)
  more/JJR
  than/IN
  (NP###### the/DT standard/JJ combination/NN)
  (NP###### therapy/NN)
  in/IN
  (NP###### a/DT late-stage/JJ trial/NN)
  ./.)
  '''
