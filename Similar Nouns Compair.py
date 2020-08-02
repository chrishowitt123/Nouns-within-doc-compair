#!/usr/bin/env python
# coding: utf-8

# In[22]:


import docx2txt
from collections import Counter
import pandas as pd
from textblob import TextBlob
import itertools
from rapidfuzz import fuzz
from rapidfuzz import process


text =  docx2txt.process('MY COPY_Final HLA.P.1631_Adenda do EIA do Bloco 17_20200620 - Copy EN (1).docx')
blob = TextBlob(text)    
nouns = blob.noun_phrases
orderedNouns = Counter(nouns).most_common()

nouns = []
values= []


for n, v in orderedNouns:
    nouns.append(n)
    values.append(v)

orderedNouns = pd.DataFrame(list(zip(nouns, values)),
              columns=['Nouns','Score'])

x_list = []
y_list = []
score = []


for x,y in itertools.combinations(nouns, 2):
    fuzz.ratio(x, y)
    score.append(fuzz.ratio(x, y))
    x_list.append(x)
    y_list.append(y)
    
data_tuples = list(zip(x_list,y_list,score))

results = pd.DataFrame(data_tuples, columns=['X','Y', 'Score'])  
results = results.sort_values(by=['Score'], ascending=False)
results = results[results['Score'] > 70]
results.to_csv('nounsSim.csv')


# In[23]:


orderedNouns


# In[26]:


import itertools
from rapidfuzz import fuzz
from rapidfuzz import process

x_list = []
y_list = []
score = []


for x,y in itertools.combinations(nouns, 2):
    fuzz.ratio(x, y)
    score.append(fuzz.ratio(x, y))
    x_list.append(x)
    y_list.append(y)
    
data_tuples = list(zip(x_list,y_list,score))

results = pd.DataFrame(data_tuples, columns=['X','Y', 'Score'])  
results = results.sort_values(by=['Score'], ascending=False)
results = results[results['Score'] > 70]
results.to_csv('nounsSim.csv')


# In[ ]:




