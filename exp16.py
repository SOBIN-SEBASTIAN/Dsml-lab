from nltk import bigrams, word_tokenize
from nltk.util import ngrams
from nltk.lm import Laplace
sentence = "Natural language proceimport nltkssing is fascinating."
words = word_tokenize(sentence)
bigrams_list = list(bigrams(words))
print("\n N-gram Modeling:")
print(bigrams_list)
sentence = "Natural language processing is fascinating."
words = word_tokenize(sentence)
bigrams_list = list(ngrams(words, 2))
lm = Laplace(order=2)
lm.fit([bigrams_list], vocabulary_text=words)
probability = lm.score("natural", "language")
print("\nSmoothing:")
print(f"Probability of 'natural language': {probability}")
