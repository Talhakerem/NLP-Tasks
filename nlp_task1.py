import nltk
from textblob import  TextBlob, Word
from nltk import sent_tokenize,word_tokenize
from nltk.stem import WordNetLemmatizer

string = "One of the key advantages of ChatGPT over popular translation tools like Google Translate is its ability to accurately consider the context of a text when generating translations."



#tokenize with nltk
print("-----------NLTK-----------")
token_nltk = nltk.word_tokenize(string)
print(token_nltk)
#lematize with nltk
print("lematize")
wnl = WordNetLemmatizer()
lemmatized = ' '.join([wnl.lemmatize(w) for w in token_nltk])
print(lemmatized)




#tokenize with textblob
print("-----------textblob-----------")
print(TextBlob(string).words)
sent = TextBlob(string)
#lematize with textblob
print("lematize")
lemmatized = " ". join([w.lemmatize() for w in sent.words])
print(lemmatized)
