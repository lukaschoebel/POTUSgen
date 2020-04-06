import re
import time
import random
from helpers import cleanup_result


def generate_ngram_successors(text, N):
    """Splitting the .txt file into a list of sublists of size N (N-Grams)

    :param text: Parsed twitter messages as String
    :param N: Number of N
    :returns ngram_successors: 

    """

    # Initialize ngram_successors as a list
    ngram_successors = []
    
    # TODO: ['i', 'will', 'be', 'leaving', 'florida']
    # Splitting up the input file into a list of strings
    words = text.split(" ")
    
    # TODO: [['i', 'will', 'be'], ['will', 'be', 'leaving'], ['be', 'leaving', 'florida']] with N=3
    # Splitting all words into sublists of length N
    # and appending these to ngram_successors
    for i in range(len(words) - N + 1):
        ngram_successors.append(words[i : i + N])
    
    return ngram_successors


def calculate_ngram_freqs(ngrams):
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

def next_word_max(prev_seq, N, counts):
    """Returns the word with the highest occurence given a word sequence

    :param prev_seq: 
    :param N: 
    :param counts: 
    :returns max_successor

    """

    token_seq = " ".join(prev_seq.split()[-(N-1):])

    # TODO:
    max_successor = max(counts[token_seq].items(), key=lambda k: k[1])[0]

    return max_successor

def next_word_weighted(prev_seq, N, counts):
    """Outputs the next word by taking the a weighted choice of the most recent tokens

    :param prev_seq: 
    :param N: 
    :param counts: 

    """

    token_seq = " ".join(prev_seq.split()[-(N-1):])
    choices = counts[token_seq].items()

    total = sum(weight for choice, weight in choices)
    
    successors, frequencies = zip(*list(choices))
    
    # IDEA: Obtain top k values
    # count = collections.Counter(nums)   
    # return heapq.nlargest(k, count.keys(), key=count.get) 

    next_word = random.choices(population=successors, weights=[f / total for f in frequencies], k=1)

    return next_word[0]

def gen_sentence(data, N=3):
    """Generate a random sentence based on text input file

    :param data: 
    :param N:  (Default value = 3)
    :param sentence_count:  (Default value = 5)
    :param start_seq:  (Default value = None)

    """

    # Generate successors and calculate frequencies
    ngrams = generate_ngram_successors(data, N)
    counts = calculate_ngram_freqs(ngrams)

    # Randomize start sequence and amount of sentences
    sentence_count = random.randint(2, 5)
    start_seq = random.choice(list(counts))
    generated_text = start_seq.lower()
    sentences = 0

    while sentences < sentence_count:
        generated_text += " " + next_word_weighted(generated_text, N, counts)
        sentences += 1 if generated_text.endswith(('.','!', '?')) else 0

    return cleanup_result(generated_text)


def load_data(filepath):
    """Load the tweet data as string and splitting it into words

    :param filepath: Path to the data
    :returns data: Tweet data as a string

    """

    data = open(filepath, 'r').read()
    data = ' '.join(data.split()).lower()
    
    return data

if __name__ == "__main__":

    data = load_data("data/data.txt")

    start = time.time()

    print(gen_sentence(data))
    
    time.sleep(1)
    end = time.time()
    print(f"Runtime of the program is {end - start}")