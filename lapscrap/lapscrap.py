#!/bin/python
from __future__ import print_function # use pyton 3 print function for splitting 
                                      # when we want
import urllib2
from bs4 import BeautifulSoup
import sys
import os

# Check if argument is given on cli, else exit
if len(sys.argv) < 2:
  sys.exit('provide %s "full mylaps.com url"' % sys.argv[0])
results = sys.argv[1]

directory = "csv"
agent = ""
page = urllib2.urlopen(results)
soup = BeautifulSoup(page, 'html.parser')
title = soup.find('title')
title = title.text
title = title.replace(" ", "_")
title = title.replace("|", "")

if not os.path.exists(directory):
  os.makedirs(directory)
os.chdir(directory)  
f = open(title+".csv", "w")

list =  []
headers = []
participant = 0
element = 0

for header in soup.find_all('th'):
    header = header.text
    header = header.strip()
    headers.append(header)

count = 0
for i in headers:
  count = count + 1
  print(i, ",", end="", file=f)
  if count == len(headers):
        print ("", file=f)
elementen = len(headers)

for row in soup.find_all('tr'):
    for col in row.find_all('td'):
      col = col.text.encode('utf-8').decode('ascii', 'ignore')
      col = col.strip()   # Strip newline from element
      col = col.lstrip() 
      list.append(col)

# First 4 elements of list we need to remove, it is clutter
del list[0:4]
list.reverse() # reverse list to delete last elements
del list[0:4] # Last 4 elements of list we don't need
list.reverse() # Reverse back, pretty ugly

count = 0
for i in list:
  print (i, ",", end="", file=f)  
  count = count + 1   
  if count == elementen:
     participant = participant + 1
     count = 0
     print ("", file=f)

f.close
