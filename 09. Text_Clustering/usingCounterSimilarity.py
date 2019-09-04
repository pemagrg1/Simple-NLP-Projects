listA = ['apple', 'orange', 'apple', 'apple', 'banana', 'orange'] # (length = 6)
listB = ['apple', 'orange', 'grapefruit', 'apple'] # (length = 4)
listC=['mango','pineapple','guava']
from collections import Counter
counterA=Counter(listA) #unique ones
counterB=Counter(listB)
counterC=Counter(listC)
print(counterA)
print(counterB)
import math

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

print("AnB",counter_cosine_similarity(counterA, counterB))
print("AnC",counter_cosine_similarity(counterA, counterC))
