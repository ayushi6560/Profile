import os
import csv
from pdfminer.high_level import extract_text
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer 
import collections
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
 


pdf_names = []
text_list = []


directory = '/home/ayu/Desktop/profile/resume'
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdf_names.append(filename)


for pdf in pdf_names:
    text = extract_text(pdf)
    text.replace("\n","")
    text_list.append(text)


# function to find the top 10 most occuring word in document
def top10_words(text):
    
    text = "".join(t for t in text if t not in ("?", ".", ";", ":", "!","&","(",")",",","-"))
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    counts =  collections.Counter(tokens_without_sw)
    return [elem for elem, _ in sorted(counts.most_common(),key=lambda x:(-x[1], x[0]))[:10]]

# printing the frequent and essential words for each text using loop.

for text in text_list:
    
    lst = text.split(" ")
    tfIdfVectorizer=TfidfVectorizer(use_idf=True)
    tfIdf = tfIdfVectorizer.fit_transform(lst)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    
    # print the top 10 most occurring word in the document
    print(top10_words(text))
    
    # print the top 5 essential word using tf-idf
    print (df.head(5))
    
    



