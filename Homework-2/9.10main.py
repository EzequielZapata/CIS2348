# Ezequiel Zapata PSID: 001863257

# part 1 program that outputs the words and the amount of times they appear in a file using the csv.reader method.
# First we import csv, create a file name and a word frequency dictionary.

import csv

fileName = input()

wordsFrequency = {}

# part 2 now we read the file and add the words not yet in the dictionary, to the dictionary, and adding 1 to every word
# that repeats.
with open(fileName, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for word in row:
            if word not in wordsFrequency.keys():
                wordsFrequency[word] = 1
            else:
                wordsFrequency[word] += 1

for key in wordsFrequency.keys():
    print(key + ' ' + str(wordsFrequency[key]))