#Regex
import re

#Get list of all sentences in document
sentences = []
with open ("input.txt") as document:
    for line in document:

        #Add contained sentences to list (Currently assumes no abbreviations, acronyms, websites, decimals etc.) (Also not great at newlines.)
        sentences.extend(re.split(r"\.|\?|\!", line))

        print(sentences)
