import unittest
from timeout_decorator import *
from behavior.ngram_solutions import *
from structural import structural_helpers
try:
    from assignment import POTUSgen
    importFlag = True
except:
    importFlag = False


class TestStructural(unittest.TestCase):
    TIMEOUT_CONSTANT = 180
    time_error = f"Importing the notebook took more than {TIMEOUT_CONSTANT} seconds. This is longer than expected. Please make sure that every cell is compiling and prevent complex structures."
    import_error = "There seems to be an error in the provided notebook. Please make sure that every cell is compiling without an error."
    method_error = "Function %s could not be found. Please don\'t rename the methods."
    
    @timeout_decorator.timeout(TIMEOUT_CONSTANT, timeout_exception=TimeoutError, exception_message=time_error)
    def test_notebook_import(self):
        if (importFlag is False):
            raise ImportError(self.import_error)
        else:
            pass

    def test_check_function_names(self):
        self.assertIs(structural_helpers.check_for_function('generate_ngram_successors', POTUSgen), True,
                        self.method_error % ('generate_ngram_successors'))
        self.assertIs(structural_helpers.check_for_function('calculate_ngram_freqs', POTUSgen), True,
                        self.method_error % ('calculate_ngram_freqs'))
        self.assertIs(structural_helpers.check_for_function('next_word_max', POTUSgen), True, 
                        self.method_error % ('next_word_max'))