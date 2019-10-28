# Resilient NLP integration Design
NLP intgration uses Nature Language Processing to digests incident data, and
provide advanced search service.

## Classes
UML class diagram:

![UML Class](./images/nlp_class.png)

### Res-ml
Command line script to build NLP model

### NLPWord2Vec
NLP super class using gensim word2vec to build a NLP model

### ResSIF
Compute word counts for dataset. Used in Smooth Inverse Frequency (SIF)
calculation

### ResSen2Vec
Compute a vector an input sentence, using word2vec and SIF

### ResNLP
Subclass of NlpWord2Vec. Implements logic to preprocess incident data
