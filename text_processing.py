import string
import nltk
ps = nltk.PorterStemmer()
stopwords = nltk.corpus.stopwords.words("english")

def normalize(string):
    return string.lower()

def remove_punc(str):

    reduced = []
    for char in str:
        if char not in string.punctuation:
            reduced.append(char)
    return "".join(reduced)

def tokenize(string):
    return string.split()

def stemm(string):
    return ps.stem(string)

def remove_stop_words(list):
    cleaned_text = []
    for word in list:
        if word not in stopwords:
            cleaned_text.append(stemm(word))
    return cleaned_text