#Import Regex
import re
import collections

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
    words = re.findall(r"[\w']+", sentence)

    #Build phrases starting from each word
    for index,word in enumerate(words):

        #Start with smallest phrase length and increase in size until end of sentence
        phrase_length = min_phrase;
        while (phrase_length <= max_phrase and  index + phrase_length <= len(words)):

            #Phrases are all words between current index and phrase length
            phrase = ' '.join( words[index : (index + phrase_length)] )

            #Add phrase to dictionary or increment dulplicate count if it already exists
            phrases[phrase] = phrases.get(phrase, 0) + 1
            phrase_length += 1


print(phrases)
    #print(words) #Debug