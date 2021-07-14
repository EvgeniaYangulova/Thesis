# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:37:05 2021

@author: midni
"""
import random
import math

# Configure paths to your dataset files here
DATASET_FILE = 'punctuation.txt'
FILE_TRAIN = 'punctuation_train.txt'
FILE_VALID = 'punctuation_dev.txt'
FILE_TESTS = 'punctuation_test.txt'


# Make sure it adds to 100, no error checking below
PERCENT_TRAIN = 70
PERCENT_VALID = 20
PERCENT_TESTS = 10

data = [l for l in open(DATASET_FILE, 'r', errors="ignore")]

train_file = open(FILE_TRAIN, 'w')
valid_file = open(FILE_VALID, 'w')
tests_file = open(FILE_TESTS, 'w')


num_of_data = len(data)
num_train = int((PERCENT_TRAIN/100.0)*num_of_data)
num_valid = int((PERCENT_VALID/100.0)*num_of_data)
num_tests = int((PERCENT_TESTS/100.0)*num_of_data)

data_fractions = [num_train, num_valid, num_tests]
split_data = [[],[],[]]

rand_data_ind = 0

for split_ind, fraction in enumerate(data_fractions):
    for i in range(fraction):
        rand_data_ind = random.randint(0, len(data)-1)
        split_data[split_ind].append(data[rand_data_ind])
        data.pop(rand_data_ind)

for l in split_data[0]:
    train_file.write(l)
    
for l in split_data[1]:
    valid_file.write(l)    
    

for l in split_data[2]:
    tests_file.write(l)
    
train_file.close()
valid_file.close()
tests_file.close() 