#Import Regex
import re

#Settings
min_phrase = 4
max_phrase = 10

#Get list of all sentences in document
sentences = []
with open ("input.txt") as document:
    for line in document:

        #Add contained sentences to list (Currently assumes no abbreviations, acronyms, websites, decimals etc.) (Also not great at newlines.)
        sentences.extend(re.split(r"\. |\?|\!", line))

        #print(sentences) #Debug

#Build dictionary of phrases
phrases = {}
for sentence in sentences:
    words = re.split('\W+', sentence)

    print(words) #Debug