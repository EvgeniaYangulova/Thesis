# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:58:17 2021

@author: midni
"""


def extract_errors():
    original_sentence = []
    index_list = []
    with open("verb_form_gold.m2", "r", errors="ignore") as file:
        first_line = file.read().splitlines() 
    for element in first_line:
        empty_line_index = first_line.index('')
        first = ' '.join(first_line[:empty_line_index])
        original_sentence.append(first)
        del first_line[:empty_line_index + 1]
    for sentence in original_sentence:
        if sentence.count("OTHER") == 0 and sentence.count("VERB:FORM") >= 0:
            index_list.append(original_sentence.index(sentence))
    return index_list
        
def extract_corrected_sentences():
    corrected_sentence= ""
    index_sentence = extract_errors()
    with open("verb_form_corrected.txt", "r", errors="ignore") as file:
        lines = file.read().splitlines() 
    for index in index_sentence:
        corrected_sentence += lines[index] + "\n"
    with open("verb_form_filtered_corrected.txt", "w") as file:
        file.write(corrected_sentence)
        
def get_original_sentences():
    original_sentence= ""
    index_sentence = extract_errors()
    with open("verb_form_original.txt", "r", errors="ignore") as file:
        lines = file.read().splitlines() 
    for index in index_sentence:
        original_sentence += lines[index] + "\n"
    with open("verb_form_filtered_original.txt", "w") as file:
        file.write(original_sentence)
    
print(get_original_sentences())