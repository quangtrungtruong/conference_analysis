import re
from bs4 import BeautifulSoup
import urllib.request as urllib2
from collections import Counter
from pyexcel_io import save_data
from collections import OrderedDict
import pandas as pd

user_input = ''

with urllib2.urlopen("https://cvpr.thecvf.com/Conferences/2024/AcceptedPapers") as f:
    contents = f.read().lower()

soup = BeautifulSoup(contents, 'lxml')

# while True:
#     user_input = input('Do you want to continue? yes/no. If yes, type keyword: ')
#
#     if user_input.lower() == 'no' or user_input.lower() == 'n':
#         print('User typed no')
#         break
#     else:
#         kw = user_input.lower()
#
#         tags = soup.find_all(['strong', 'i'])
#         papers = soup.find_all('strong')
#         authors = soup.find_all('i')
#         res = soup.find_all(string=re.compile(kw))
#
#         print("==============================================")
#
#         if kw=="all":
#             for id, r in enumerate(papers):
#                 print(id, ' '.join(r.text.split()))
#         else:
#             for id, r in enumerate(res):
#                 print(id, ' '.join(r.text.split()))


soup = BeautifulSoup(contents, 'lxml')
papers = soup.find_all('strong')
sentence = ""
for p in papers:
    sentence += ' ' + p.text
words = re.findall(r'\w+', sentence)

data = OrderedDict()
words2 = [' '.join(ws) for ws in zip(words, words[1:])]
words3 = [' '.join(ws) for ws in zip(words, words[1:], words[2:])]
words4 = [' '.join(ws) for ws in zip(words, words[1:], words[2:], words[3:])]
words5 = [' '.join(ws) for ws in zip(words, words[1:], words[2:], words[3:], words[4:])]
words6 = [' '.join(ws) for ws in zip(words, words[1:], words[2:], words[3:], words[4:], words[5:])]

d = [(w, f) for w, f in Counter(words6).most_common() if f > 1]
df = pd.DataFrame(d, columns=['Phrase', 'Frequencies'])
df.to_html(open('cvpr.html','w'))

d = [(w, f) for w, f in Counter(words5).most_common() if f > 1]
df = pd.DataFrame(d, columns=['Phrase', 'Frequencies'])
df.to_html(open('cvpr.html','a'))

d = [(w, f) for w, f in Counter(words4).most_common() if f > 1]
df = pd.DataFrame(d, columns=['Phrase', 'Frequencies'])
df.to_html(open('cvpr.html','a'))

d = [(w, f) for w, f in Counter(words3).most_common() if f > 2]
df = pd.DataFrame(d, columns=['Phrase', 'Frequencies'])
df.to_html(open('cvpr.html','a'))

d = [(w, f) for w, f in Counter(words2).most_common() if f > 3]
df = pd.DataFrame(d, columns=['Phrase', 'Frequencies'])
df.to_html(open('cvpr.html','a'))