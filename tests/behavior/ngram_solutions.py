"""
@author: Lukas Schöbel 2019.
"""

import re
import random
from helpers import cleanup_result

def load_test_data():
    """Load the tweet data as string and splitting it into words

    :returns data: Tweet data as a string

    """
    
    filename = "data/test_data.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        s = file.read()
        s = ' '.join(s.split()).lower()
        return s

def generate_ngram_successors_solution(text, N):
    """Splitting the .txt file into a list of sublists of size N (N-Grams)

    :param text: Parsed twitter messages as String
    :param N: Number of N
    :returns ngram_successors: 

    """

    # Initialize ngram_successors as a list
    ngram_successors = []
    
    # Splitting up the input file into a list of strings
    words = text.split(" ")
    
    # Splitting all words into sublists of length N
    # and appending these to ngram_successors
    for i in range(len(words) - N + 1):
        ngram_successors.append(words[i : i + N])
    
    return ngram_successors


def calculate_ngram_freqs_solution(ngrams):
    """Calculate the frequency of a subsequent word given a sequence of ngrams

    :param ngrams: [['i', 'will', 'be'], ['will', 'be', 'leaving'], ['be', 'leaving', 'florida']]

    """

    freqs = {}

    for ngram in ngrams:
        # Differentiate successor (= lastWord) ...
        successor = ngram[-1]

        # ... from the ngram sequence
        ngram_seq  = " ".join(ngram[:-1])

        # If a given sequence is not known, initialize 
        # an empty hash map for ngram_seq.
        if ngram_seq not in freqs:
            freqs[ngram_seq] = {}

        # If successor not seen, set th count for 
        # the successor and the given sequence to 0.
        if successor not in freqs[ngram_seq]:
            freqs[ngram_seq][successor] = 0
        
        # Increase frequency of successor given the sequence
        freqs[ngram_seq][successor] += 1

    return freqs


def next_word_max_solution(prev_seq, counts, N):
    """Returns the word with the highest occurence given a word sequence

    :param prev_seq: 
    :param counts:
    :param N:  
    :returns max_successor

    """

    token_seq = " ".join(prev_seq.split()[-(N-1):])

    # SOLUTION: 
    max_successor = max(counts[token_seq].items(), key=lambda k: k[1])[0]

    return max_successor

def check_next_word_max(data, start_seq, N, max_func=next_word_max_solution):
    """Checks the previous function implementations
    
    :param data: Loaded twitter messages
    :param start_seq: Loaded twitter messages
    :param N: nGram parameter
    :returns generated_text: Cleaned up message as a String
    
    """
    
    sentences = 0
    ngrams = generate_ngram_successors_solution(data, N)
    counts = calculate_ngram_freqs_solution(ngrams)
    
    generated_text = start_seq.lower()
    
    while sentences < 1:
        generated_text += " " + max_func(generated_text, counts, N)
        sentences += 1 if generated_text.endswith(('.','!', '?')) else 0
    
    return cleanup_result(generated_text)

def cleanup_result(s):
    """Cleans a given string and fixes punctuation and capitalization

    :param s: 

    """

    # Whitespace & Padding correction
    s = re.sub('\\s+([.,!?])\\s*', r'\1 ', s)
    s = re.sub(r' ([\,\.\/\-\"\?\!\:\;])', "\\1", s)
    s = re.sub(r'( [a-zA-Z]) . ([a-zA-Z]) .', "\\1.\\2.", s)

    # Capitalization correction
    s = s.capitalize()
    s = re.sub(" i[,;!]? ", " I ", s)
    s = re.sub('([.!?]\\s+[a-z])', lambda c: c.group(1).upper(), s)
    
    return s