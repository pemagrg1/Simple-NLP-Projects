"""
INSTALLATIONS: 
  pip install neuralcoref --no-binary neuralcoref
  pip install -U spacy
  python -m spacy download en
"""

import neuralcoref
import spacy

nlp = spacy.load('en')
# Add neural coref to SpaCy's pipe
neuralcoref.add_to_pipe(nlp)

# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
doc = nlp(u'My sister has a dog. She loves him.')

print(doc._.has_coref)
print(doc._.coref_clusters)

"""
result:
True
[My sister: [My sister, She], a dog: [a dog, him]]
"""
