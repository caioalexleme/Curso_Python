from os import path
from os import listdir
from pydash import _
from future.utils import viewitems
from random import random
from app.exceptions.base_exceptions import DefaultException
import re
import os

def get_words_by_category(filepath):
    words_by_category = {}
    def recurse_words_tree(filepath):
        filepath = path.abspath(path.join(os.getcwd(), filepath))
        if not path.exists(filepath):
            raise DefaultException('\'' + filepath + '\' path does not exist')
        matches = re.findall(r'\/[^\/\.]+', filepath)
        category = matches[len(matches) - 1][1:]
        if not path.isdir(filepath):
            with open(filepath, 'r') as f:
                words = list()
                for line in f.readlines():
                    word = line[:len(line) - 1]
                    if len(word) > 0:
                        words.append(line[:len(line) - 1])
                if category in words_by_category:
                    words_by_category[category] = _.flatten([words, words_by_category[category]])
                else:
                    words_by_category[category] = words
                return { category : f.readlines() }
        words = list()
        for item in listdir(filepath):
            words.append(recurse_words_tree(path.join(filepath, item)))
        return { category: words }
    recurse_words_tree(filepath)
    return words_by_category

def get_words(path, category):
    words_by_category = get_words_by_category(path)
    if category:
        if not category in words_by_category:
            raise DefaultException('\'' + category + '\' category does not exist')
        return words_by_category[category]
    words = list()
    for (key, item) in viewitems(words_by_category):
        for word in words_by_category[key]:
            if not _.includes(words, item):
                words.append(word)
    return words

def get_random_words(path, category=None, count=1):
    words = get_words(path, category)
    if count > len(words):
        count = len(words)
    random_numbers = get_random_numbers(count, len(words))
    random_words = list()
    for random_number in random_numbers:
        random_words.append(words[random_number])
    return random_words

def get_random_numbers(count, length):
    random_numbers = list()
    for i in range(count):
        random_number = int(random() * length)
        if _.includes(random_numbers, random_number):
            random_number = get_next_unique_number(length, random_numbers, random_number)
        random_numbers.append(random_number)
    return random_numbers

def get_next_unique_number(length, numbers, number):
    number = (number + 1) % length
    if _.includes(numbers, number):
        number = get_next_unique_number(length, numbers, number)
    return number

def get_categories(path):
    words_by_category = get_words_by_category(path)
    categories = list()
    for (key, item) in viewitems(words_by_category):
        categories.append(key)
    return categories
