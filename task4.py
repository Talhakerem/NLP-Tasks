import nltk, re
from collections import Counter
from nltk.corpus import stopwords

def delete_words(string):
 stop_words = set(stopwords.words('turkish'))
 words = string.split()
 filtered_words = [word for word in words if word not in (stop_words)]
 return ' '.join(filtered_words)


f = open("tur_wikipedia_2021_10K-sentences.txt","r",encoding="utf-8")
string = f.read()
string = delete_words(string)
string = re.sub(r"[-()\"#/@;:<>{}`+=~|&.!?,’']", "", string)
token = nltk.word_tokenize(string)
tags = Counter(nltk.pos_tag(token))

for tag,count in tags.most_common(20):
 print(tag,count)

