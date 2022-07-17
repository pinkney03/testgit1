import json
import nltk
from textblob import TextBlob
import re
import collections as cl
import time
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('averaged_perceptron_tagger')

import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')


# taking input text as India
text = "drive"
ans = nltk.pos_tag([text])

# ans returns a list of tuple
val = ans[0][1]
print(ans)

# checking if it is a noun or not
if (val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
    print(text, " is a noun.")
else:
    print(text, " is not a noun.")

def cleanwords(w):
    result=nltk.pos_tag(w)
    #print(result)
    return result
r=cleanwords(['drive'])
v=TextBlob('drive')
print(r,v.noun_phrases)

from nltk.corpus import wordnet
words = ["would","research","drive","part","technologies","size","articles","analyzes","line"]
for w in words:
    syns = wordnet.synsets(w)
    for i in range(len(syns)):
        print(w, syns[i].lexname().split('.')) if syns else (w, None)