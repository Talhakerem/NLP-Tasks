from nltk.corpus import reuters,gutenberg,stopwords
import nltk, re
from collections import Counter

def delete_words(string):
    stop_words = set(stopwords.words('english'))
    words = string.split()
    filtered_words = [word for word in words if word not in (stop_words)]
    return ' '.join(filtered_words)


string = gutenberg.raw()
#string = reuters.raw()


string = string.lower()
string = re.sub(r"[-()\"#/@;:<>{}`+=~|&.!?,’']", "", string)
print(string)
string = delete_words(string)

print(string)
token = nltk.word_tokenize(string)


bigrams = nltk.ngrams(token,2)
trigrams = nltk.ngrams(token,3)

threshold = 10
ngram_freq = nltk.FreqDist(trigrams)
for k,count in ngram_freq.items():
    if count>threshold:
        print(k,count)


tags = Counter(nltk.pos_tag(token))
print("Post Tags")
for tag,count in tags.most_common(10):
    print(tag,count)
