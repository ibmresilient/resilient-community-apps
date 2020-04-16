# Design for Resilient Machine Learning NLP Integration 
The Resilient Machine Learning NLP integration supports using Nature Language Processing (NLP) to digest incident
textual data, and provides advanced predictions of incident relationships.

## NLP
To obtain the relationship among incidents, an NLP model is used to process textual information
of incidents, including the following:
* name
* description 
* resolution summary 
* artifact descriptions
The goal is to find similar incidents based on the above information.

In order to find a relationship between textual information, one approach is to find a relationship between
individual words first. This NLP integration uses a Python package called gensim word2vec to do so.

### Word Embeddings
[Gensim word2vec](https://radimrehurek.com/gensim/models/word2vec.html) represents each word used 
in the dataset as a multi-dimensional vector. This is also
called word embeddings. Here the dataset is the textual information of all the incidents. This is the
dataset being used to train the word2vec model. Note that this is an unsupervised learning model, so
we do not need to split the dataset into training and testing. The whole set is used for training.

From the dataset, the word2vec model looks for the likelihood that words co-occur in proximity. 
Using this information,
the model can convert each word into a vector such that similar words would stay close to 
each other. This is a two-layer neural network model, which is not so computationally expensive. 

To understand how a word can be represented by a vector, it might be helpful to imagine that each dimension of the 
vector space represents something meaningful and understandable. 
![nlp_meaning](images/nlp_meaning.png)
Each word is then a combination (vector sum) of those meaningful features. Similar words should then have 
similar combination, and thus stay close to each other.
   
In reality, users specify how many features to use, and the model figures out what features to use.
A dimension used by a word2vec model is, in general, a combination of several meaningful features 
human being can understand. 

For the Resilient Machine Learning NLP integration, the default number of features is set to 50. Advanced users can change this value in 
app.config.

There are other (advanced) settings for word2vec stored in nlp_settings.py. They are for advanced users
to fine-tune the word2vec model, if they are familiar with it.

In summary, word2vec can convert words into multidimensional vectors. Similar words stay close to each
other. Similarity between words can then be defined as a dot product of the corresponding vectors.

### Sentence similarity
Word2vec can find out the similarity between words. But how about sentences?

Remember that the similarity between two words is computed by the dot product of those two
corresponding vectors. 

A simple approach is to represent a sentence using the sum of the vectors of all the words. It turns 
out this simple approach can give useful results, with small enhancements, according to this [research
result](https://openreview.net/pdf?id=SyK00v5xx) from Princeton University.

The enhancements includes:
* Use Smooth Inverse Frequency (SIF) to lower the contribution of common words
* Remove the principle component of each vector

#### SIF
When word vectors are summed up, a weight factor is assigned to each word. 
```
a/(a+wc)
```
Here ```a``` is a small number (10^(-4)) and wc is the word count. As shown above, the bigger the word count, the smaller
the weight factor. To understand this, imagine a word appears in all samples (incidents), then this
word is not useful at all in distinguishing different incidents. 
Thus higher word count shall go with lower contribution.

#### Remove PCA
According to the research research paper from Princeton University, the vectors for sentences obtained by summing word vectors
all share a common principle component (vector), due to shared common words. By removing this common component,
this model can give more a more accurate result.

With these two enhancements, word2vec can be used to obtain similarity between sentences.

### Resilient NLP summary
In summary, the steps to build a Resilient NLP model can be summarized in the following data flow
diagram:
![data flow](images/NLP_dataflow.png)

* The raw data (incidents) is used as training dataset to build a gensim word2vec model. The result is saved into
a .txt file. By default, this file is named resilient-w2v.txt.
* The raw data is used to get word count. The data is saved into a file called resilient-sif.pkl. 
* The raw data and the above generated data are used to get sentence vectors.
* PCA is then computed using the sentence vectors. PCA data is saved into resilient-pca.json.
* PCA is removed from each sentence vector, and all sentence vectors are saved into resilient-vec.json.

Later on, to find similar incidents given a new one, we need to use all four files saved above,
as shown in the following data flow diagram.
![dat flow](images/NLP_search_dataflow.png)
* Use the resilient-w2v.txt file to find the vector for each word of the new incident.
* Use the resilient-sif.pkl file to find the weight factor for each word.
* Sum up the word vector to get the sentence vector.
* Remove PCA vector (saved in resilient-pca.json) from the sentence vector above.
* Compute the dot product of this new sentence vector and each sentence vector saved in resilient-vec.json.
* Find the top ones.

## Classes
UML class diagram:

![UML Class](./images/nlp_class.png)

### Res_ml
Command line script to build an NLP model. It instantiates a ResNLP object to do so. It provides the following two subcommands:

#### build_nlp
This subcommand builds an NLP model. It calls ResUtils functions to download incidents and artifacts then saves them 
into resilient-incidents.csv and resilient-artifacts.json. Then it calls ResNLP to build an NLP model. The model is 
saved as the following files, as mentioned in the data flow diagram.

* resilient-w2v.txt: word2vec model in text format. It is basically a word-vec dictionary.
* resilient-sif.pkl: word count in python pickle format. It is a word-count dictinary.
* resilient-vec.json: vectors for all (old) incidents. 
* resilient-pca.json: a vector for the principle component, in json format.
 
At the end, it removes the saved incident and artifact files.

#### view
This subcommand displays summary information of an input file. An input file must
be one of those four files listed above. 

### ResNLP
ResNLP extends NLPWord2Vec and implements logic to preprocess incident data. Several
important methods of this class are listed below.

#### load_data
This method loads the incident and artifact data from files. Note these are the input
data used to build the NLP model.

#### preprocess_data
In the method, the input data is pre-processed. First, for an incident, textual data 
is concatenated together. Then WordSentenceUtil is used to extract a list of words for each 
incident.

#### build
This method builds the word2vec model and the SIF word count.

It calls the build_model of its superclass to build the word2vec model.

#### save
This method saves the model into files.

### NLPWord2Vec
NLP base class encapsulates gensim word2vec for a NLP model. It is a super class
of ResNLP.

#### build_model
This is the standard process of building aword2vec model.

#### get_word_vec
Once a word2vec model is built, this method can provide the vector for a given word. 

### ResSIF
Computes word counts for the dataset. Used in Smooth Inverse Frequency (SIF)
calculation.

#### build_sif
Builds the word count for a given dataset, which is a list of a list of words. 
Each incident is represented as a list of words. Therefore, a list of incidents becomes
a list of a list of words.

Word count is stored in a dictionary of word-count pairs.

#### save_sif
Saves SIF into a file.

#### load_sif
Loads SIF from a file.

#### get_word_count
Returns the count of a given word.

### ResSen2Vec
Computes a vector of an input sentence, using word2vec and SIF.

#### get_vec_for_words
For a given list of words, computes and returns the vector.

It uses the ResNLP to figure out the vector for each word, the ResSIF to figure out the contribution weight 
factor, then sums up the vectors.

#### get_vec_for_sentence
For a given sentence, it calls WordSentenceUtils to extract a list 
of words from it. Then it calls its get_vec_for_words to get the
corresponding vector.  

#### remove_pca
Once we get the vectors for all the (old) incidents, we can compute the PCA
for them. 

Then this method removes the PCA from each vector. It also saves the PCA for later
use.


### cache_sentence_vectors
This method takes the incident data (a list of a list of words), and computes
the vectors. Then it calls remove_pca to remove/save PCA. Then it saves the 
vectors. 

#### get_closeset
This is the main method to get the similar incidents. 

Inputs:
* sentence: Description of the newly created incident.
* num: How many similar incidents to return.
* other incidents: Important here. When a NLP model is built, vectors are computed/saved for each incident
created so far. Later on, the NLP model is used to do a search. But there is a time gap between
when the model is built, and when the model is used to do a search. Incidents could
have been created within this time period. These incidents are not in a saved vector file. 
We need to download them separately, and input them here.
* search_inc_id: Incident ID of the newly created incident. Because the newly created incident
is created after the model is built, it is included in the "other incident". Because it is very similar
to itself, its similarity is very high. We want to exclude this from the return. 

#### find_key_words
A general problem of ML and NLP is that sometimes why a model makes a certain decision is quite opaque.
For our case here, why a model picks one incident as a similar one instead of another is not always very clear.

This method tries to get some insights. Remember that the vector for an incident is computed as sum of word
vectors. When NLP concludes a newly created incident (call it incident a), is similar to an old incident (call it incident b),
we want to know which words in incident a make the biggest contribution. 

To do so, we compute the similarity between incident b and each word of incident a. It is basically the dot product
between a sentence vector and a word vector. Those top ones contribute the most to the overall similarity, and they
can be considered as the keywords being used in the search for similar incidents. 

### WordSentenceUtils
This is a collection of utility functions. 

### get_words 
This method extracts useful words from a given sentence. It does the following:
* Uses BeautifulSoup to remove html tags.
* Removes unwanted characters such as "," and  "."
* Uses NLTK to remove normal English stop words. The current Resilient NLP supports English only.
* Uses NLTK WordNetLemmatizer to return a word to its base form, such as from "went" to "go". 

## Sequence Diagrams
Two major processes, namely building an NLP model and searching using an
NLP model.
### Build an NLP model
![build_sequence](images/nlp_build_seq.png)

### Search
![search_sequence](images/nlp_search_seq.png)