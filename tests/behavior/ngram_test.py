import re
import os
import unittest
from timeout_decorator import *
from behavior.ngram_solutions import *
from assignment.POTUSgen import generate_ngram_successors, calculate_ngram_freqs, next_word_max


class TestNotebook(unittest.TestCase):
    TIMEOUT_CONSTANT = 240
    TIME_ERROR = 'Timeout Error. %s seems to take more than 4m to execute. Please keep the computational complexity in mind.'
        
    def setUp(self):
        self.test_data = load_test_data()

    @timeout_decorator.timeout(TIMEOUT_CONSTANT, timeout_exception=TimeoutError, exception_message=TIME_ERROR % ('generate_ngram_successors()'))
    def test_generate_ngram_successors(self):
        self.assertEqual(generate_ngram_successors(self.test_data, 1), generate_ngram_successors_solution(self.test_data, 1))
        self.assertEqual(generate_ngram_successors(self.test_data, 3), generate_ngram_successors_solution(self.test_data, 3))
        
    @timeout_decorator.timeout(TIMEOUT_CONSTANT, timeout_exception=TimeoutError, exception_message=TIME_ERROR % ('calculate_ngram_freqs()'))
    def test_calculate_ngram_freqs(self):
        ngram_test_data_3 = generate_ngram_successors(self.test_data, 3)
        self.assertEqual(calculate_ngram_freqs(ngram_test_data_3), calculate_ngram_freqs_solution(ngram_test_data_3))
        
        ngram_test_data_5 = generate_ngram_successors(self.test_data, 5)
        self.assertEqual(calculate_ngram_freqs(ngram_test_data_5), calculate_ngram_freqs_solution(ngram_test_data_5))
        
    @timeout_decorator.timeout(TIMEOUT_CONSTANT, timeout_exception=TimeoutError, exception_message=TIME_ERROR % ('next_word_max()'))
    def test_next_word_max(self):
        self.assertEqual(check_next_word_max(self.test_data, "dems are", 3), check_next_word_max(self.test_data, "dems are", 3, max_func=next_word_max))
        self.assertEqual(check_next_word_max(self.test_data, "will be signing the", 5), check_next_word_max(self.test_data, "will be signing the", 5, max_func=next_word_max))
        self.assertEqual(check_next_word_max(self.test_data, "why would kim jong-un insult me by calling me old", 11), check_next_word_max(self.test_data, "why would kim jong-un insult me by calling me old", 11, max_func=next_word_max))