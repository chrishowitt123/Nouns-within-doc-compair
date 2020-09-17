
import docx2txt
from collections import Counter
import pandas as pd
from textblob import TextBlob
import itertools
from rapidfuzz import fuzz
from rapidfuzz import process
from termcolor import colored
import tkinter as tk
from tkinter import filedialog

print( "\n")  
print("Welcome to NounSim!")
print( "\n")  
print("""     ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\      
 //________.|.________\\     
`----------`-'----------'""")
print( "\n") 
answer = input('Do you need to search for your file? Y/N: ').lower()
print('\n')
if answer == 'y':
    file = filedialog.askopenfilename()

else:
    file = input('Paste the location of the file: ').strip('"')

print( "\n")
print(""" Processing.. 
      
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)   """)
    
    
print( "\n")   
print( "\n")  
print( "\n")  
print( "\n")   
    
text =  docx2txt.process(file)
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

x_list3 = list(results['X'])
y_list3 = list(results['Y'])

diffs = []


def find(X, Y):
    count = {}
    for word in X.split():
        count[word] = count.get(word, 0) + 1

    for word in Y.split():
        count[word] = count.get(word, 0) + 1
    return [word for word in count if count[word] == 1]



for X,Y in zip(x_list3, y_list3):
    diffs.append((find(X, Y)))
    
diffsList = [' '.join(x) for x in diffs]
results['Diffs'] = diffsList
results = results[['Score', 'X', 'Y', 'Diffs']]


resultsXlist = results['X'].tolist()
resultsYlist = results['Y'].tolist()
resultDIFFSYlist = results['Diffs'].tolist()
resultSCORElist  = results['Score'].tolist()




n = 0
while n <= len(resultsXlist) - 1:

    text1 = resultsXlist[n]  
    text2 = resultsYlist[n] 
    l1 = resultDIFFSYlist[n].split()

    
    
    formattedText1 = []
    for t in text1.split():
        if t in l1:
            formattedText1.append(colored(t,'red', attrs=['bold']))
        else: 
            formattedText1.append(t)

    
    formattedText2 = []
    for t in text2.split():
        if t in l1:
            formattedText2.append(colored(t,'red', attrs=['bold']))
        else: 
            formattedText2.append(t)
 
    print( "\n")
    print(colored(resultSCORElist[n], 'green'))
    print(colored(l1, 'blue'))
    print( "\n")
    print(" ".join(formattedText1))
    print( "\n")
    print(" ".join(formattedText2))
    print( "\n")
    print( "\n")
    
    n = n+1


# In[ ]:
