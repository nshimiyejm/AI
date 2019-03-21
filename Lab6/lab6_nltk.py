import nltk 
import urllib.request

print("Reading text and Tokenizing...")
response = urllib.request.urlopen('https://www.gutenberg.org/files/74/74-h/74-h.htm')
html = response.read()
print (html)