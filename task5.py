import nltk, re
from collections import Counter
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def delete_words(string):
    stop_words = set(stopwords.words('turkish'))
    words = string.split()
    filtered_words = [word for word in words if word not in (stop_words)]
    return ' '.join(filtered_words)


with open("2.txt", encoding="utf8") as f:
    string = f.read()
string = delete_words(string)
string = string.lower()
string = re.sub(r"[-()\"#/@;:<>{}`+=~|&.!?,’']", "", string)

print(string)
token = nltk.word_tokenize(string)


fdist = FreqDist(token)
print(fdist.most_common(50))

bigrams = nltk.ngrams(token,2)
trigrams = nltk.ngrams(token,3)

threshold = 3
ngram_freq = nltk.FreqDist(trigrams)
for k,count in ngram_freq.items():
    if count>threshold:
        print(k,count)
