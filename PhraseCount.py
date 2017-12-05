import re
import collections
import operator

#Settings
min_phrase = 4
max_phrase = 10
top_phrase_number = 10

#Get list of all sentences in document
sentences = []
with open ("input.txt") as document:
    for line in document:

        #Add contained sentences to list (Currently assumes no abbreviations, acronyms, websites, decimals etc.)
        line.replace('\r\n', ' ')
        sentences.extend(re.split(r"\. |\?|\!", line))

#Build dictionary of phrases
phrases = {}
for sentence in sentences:
    words = re.findall(r"[\w']+", sentence)

    #Build phrases starting from each word
    for index,word in enumerate(words):

        #Start with smallest phrase length and increase in size until end of sentence
        phrase_length = min_phrase;
        while (phrase_length <= max_phrase and  index + phrase_length <= len(words)):
            phrase = tuple( words[index : (index + phrase_length)] )

            #Add phrase to dictionary or increment dulplicate count if it already exists
            phrases[phrase] = phrases.get(phrase, 0) + 1
            phrase_length += 1

#Sort phrases by length and check duplicates for contained phrases
sorted_phrases = sorted(phrases.items(), key=len, reverse=True)
for pair in sorted_phrases:
        if pair[1] > 1 and pair[0] in phrases:
            phrase = pair[0]
            length = len( phrase )
            contained_length = length - 1

            #Check for smaller contained phrases
            while contained_length >= min_phrase:
                
                #Within bounds of parent phrase
                index = 0
                while index <= length - min_phrase:
                    #Remove contained phrase from master phrase dictionary
                    contained_phrase = phrase[index : index + contained_length]
                    if contained_phrase in phrases:
                        del phrases[ contained_phrase ]
                    index += 1

                contained_length -= 1

#Display list of 10 most duplicated phrases
duplicates = sorted(phrases.items(), key=operator.itemgetter(1), reverse=True)
for index,phrase in enumerate(duplicates):
    if index <= top_phrase_number:
        print(' '.join( duplicates[index][0] ), duplicates[index][1])