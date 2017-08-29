'''
Author: Pema Gurung
Date: 20-7-17
'''
import nltk

text="This is the beginning of the NER TEXT where it identifies names like John,Steve and organization like Samsung and Apple."
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    print("TOKENS: \n", tokens,"\n")
    token_pos = nltk.pos_tag(tokens)
    print ("TOKEN POS: \n", token_pos,"\n")
    NER = nltk.ne_chunk(token_pos)
    print ("NER:\n:",NER,"\n")
    #namedEnt.draw() #for visualization 
    
