# Resilient NLP integration Design
NLP integration uses Nature Language Processing to digest incident data, and
provide advanced predictions of incident relationships.

## Classes
UML class diagram:

![UML Class](./images/nlp_class.png)

### Res-ml
Command line script to build a NLP model. It instantiates a ResNLP object to do so.

### NLPWord2Vec
NLP base class encapsulates gensim word2vec for a NLP model

### ResSIF
Compute word counts for dataset. Used in Smooth Inverse Frequency (SIF)
calculation

### ResSen2Vec
Compute a vector an input sentence, using word2vec and SIF

### ResNLP
ResNLP extends NLPWord2Vec. Implements logic to preprocess incident data.

## Sequences
Two major processes, namely building a NLP model and searching using a
NLP model
### Build a   NLP model
![build_sequence](images/nlp_build_seq.png)

### Search
![search_sequence](images/nlp_search_seq.png)