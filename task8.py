import numpy as np
import pandas as pd
import numpy as no
from scipy.spatial.distance import cosine
from gensim import downloader as dwn
import re

model = dwn.load("glove-wiki-gigaword-300")
index2word = set(model.index_to_key)

def average_vector(sentence,model=model,num_features=300, index2word_set = index2word):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype="float32")
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec,model[word])
    if n_words > 0:
        feature_vec = np.divide(feature_vec,n_words)
    return feature_vec


df = pd.read_excel("AirlineReviews.xlsx")
df = df['ReviewBody']
#print(df[1])
print("-------------------")
for i, sent in enumerate(df):
    df[i] = re.sub(r"[-()\"#/@;:<>{}`+=~|&.!?,’']", " ", str(df[i]))
    df[i] = df[i].lower()

#print(df[1])


my_sentence = "i love it"
my_sentence_return = average_vector(my_sentence)
max_similarity = 0
for sentence in df:
    a = average_vector(sentence)
    similarity = 1-cosine(my_sentence_return,a)
    if similarity > max_similarity:
        max_similarity = similarity
        bestsentence = sentence
print(my_sentence)
print("--------------------------")
print(str(bestsentence)+"\nSimilarity: "+str(max_similarity))