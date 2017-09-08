'''
Author: Pema Gurung
Date: 5-9-17
'''
text="""Go for pearl strings or delicate multi-layer pieces when you attend a "summer wedding".While talking about "head-turning earrings", they should be equally sparkly,  but somewhat lighter in design to avoid a melodramatic look."""

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punct = ""
for char in text:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

#########USING NLTK REGEXPTOKENIZER#######
from nltk.tokenize import RegexpTokenizer
text="""Go for pearl strings or delicate multi-layer pieces when you attend a "summer wedding".While talking about "head-turning earrings", they should be equally sparkly,  but somewhat lighter in design to avoid a melodramatic look."""

tokenizer = RegexpTokenizer(r'\w+')
final_text=tokenizer.tokenize(text)
print (final_text)

#############Using replace##
text="""Go for pearl strings or delicate multi-layer pieces when you attend a "summer wedding".While talking about "head-turning earrings", they should be equally sparkly,  but somewhat lighter in design to avoid a melodramatic look."""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punct = text
for char in text:
   if char in punctuations:
       no_punct = no_punct.replace(char," ")
# display the unpunctuated string
print(no_punct)

