#importing files and necessary libraries

import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random 
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
intents_file = open(intents.json).read()
intents = json.loads(intents_file)

#tokenization method to preprocess data 

words = []
classes = []
documents = []
ignore_letters = ['!','?',',','.']
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        # add documents in the corpus
        documents.append((word, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)

#lemmatization

#lemmaztize and lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(list(set(words)))
#sort classes
classes = sorted(list(set(classes)))
#documents = combination between partterns and intents
print(len(classes), "classes", classes)
# words = all words, vocabulary
print (len(words), "unique lemmatized words", words)
# save python object in a file. we use pickle dump
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

