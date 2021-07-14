# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:03:36 2021

@author: midni
"""
import json

from nltk import sent_tokenize

def separate_original_corrected_json():
    original = ""
    data = [json.loads(line) for line in open('B.dev.json', 'r')]
    for dictionary in data:
        text = dictionary['text']
        if "?" in text:
            sentence_question = text.replace("?", "?\n")
            original += sentence_question
        elif "!" in text:
            sentence_exclamation = text.replace("!", "!\n")
            original += sentence_exclamation
        elif "." in text:
            sentence = text.replace(".", ".\n")
            original += sentence
    with open("b_dev_wi_locness_original_preprocessed.txt", "w", errors = "ignore") as file:
        file.write(original)
            
        
    
print(separate_original_corrected_json())