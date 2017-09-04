'''
Author: Pema Gurung
Date: 5-9-17
'''
text="""Go for pearl strings or delicate multi-layer pieces when you attend a "summer wedding".While talking about "head-turning earrings", they should be equally sparkly,  but somewhat lighter in design to avoid a melodramatic look."""

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

clean_text = ""
for word in text:
   if word not in punctuations:
       clean_text = clean_text + word

# display the unpunctuated string
print(clean_text)

#########USING NLTK REGEXPTOKENIZER#######
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
final_text=tokenizer.tokenize(text)
print (final_text)

