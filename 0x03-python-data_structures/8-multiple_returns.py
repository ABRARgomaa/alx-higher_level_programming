#!/usr/bin/python3
def multiple_returns(sentence):
    a = sentence[0]
    if (len(sentence) == 0):
        a = "None"
    return (len(sentence), a)
