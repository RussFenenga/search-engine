#!/usr/bin/python

import os
import re
from collections import defaultdict
from HTMLParser import HTMLParser

allWordFrequencies = list()

class WordFrequency():
    def __init__(self):

        self.wordCount = 0
        self.wordSet= set()

        self.title  = defaultdict(int)
        self.header = defaultdict(int)
        self.strong = defaultdict(int)
        self.body   = defaultdict(int)
        self.bold   = defaultdict(int)

    def appendWord(self, word, tag):

        self.wordCount += 1

        print tag

        if tag == "body":
            self.body[word] += 1
            print self.body
        elif tag in ["h1", "h2", "h3"]:
            self.header[word] += 1
        elif tag == "title":
            self.title[word] += 1
        elif tag == "strong":
            self.strong[word] += 1
        elif tag == "b":
            self.strong[word] += 1


## HTML FILE PARSING ####################################################
CURRENT_PATH = "/Users/carloe1/Desktop/cs121_project3/WEBPAGES_CLEAN/75"

class HTMLFileParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.words = WordFrequency()
        self.tags = list()
        self.tags.append("title")

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.tags.pop()
        self.tags.append(tag)
        print "Encountered a start tag:", tag
                
    def handle_endtag(self, tag):
        if tag in self.tags:
            self.tags.pop()
            print "Encountered an end tag :", tag

    def handle_data(self, data):
        for word in re.split("[^A-Za-z0-9]+", data.rstrip().lower()):
            if word != "":
                self.words.appendWord(word, self.tags[-1])

    def getWords(self):
        return self.words


def parseFile(fileName):
    file = open(fileName, "r")
    print fileName
    parser = HTMLFileParser()
    parser.feed(file.read())


def parseDocuments():
    # Get the name of all files in current path
    for root, dirs, files in os.walk(CURRENT_PATH, topdown=False):
        for name in files:
            if "." not in name:
                parseFile(os.path.join(root, name))
        

## MAIN #################################################################
if __name__ == "__main__":
    parseDocuments()

	
