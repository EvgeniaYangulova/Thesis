# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:31:50 2021

@author: midni
"""

def separate_original_corrected_txt():
    original = ""
    corrected = ""
    with open("verb_form.txt", "r", errors="ignore") as file:
        first_line = file.read().splitlines() 
        for element in first_line:
            split_line = element.split("\t")
            original += str(split_line[5]) + "\n"
            corrected += str(split_line[8]) + "\n"
    with open("verb_form_original.txt", "w") as file:
        file.write(original)
    with open("verb_form_corrected.txt", "w") as file:
        file.write(corrected)
    
print(separate_original_corrected_txt())