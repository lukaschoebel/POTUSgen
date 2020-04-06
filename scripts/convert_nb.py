import os
import sys


def convert(notebook: str):
    ''' Script for converting a provided .ipynb to a .py file
    :type: notebook: String to Jupyter Notebook
    :rtype: script: Python File
    '''
    
    fname = notebook + '.ipynb'

    # Check for renaming of the notebook
    if not os.path.exists(fname):
        raise ImportError('You seem to have renamed the notebook. Please use the original name') 
    
    # Check if notebook has already been converted
    if not os.path.exists(notebook + '.py'):
        command = 'jupyter nbconvert --to script ' + fname
        os.system(command)
        print(f'>> Sucessfully converted {fname} to {notebook}.py')

if __name__ == "__main__":

    if len(sys.argv) - 1: convert(sys.argv[1]) 
    convert('POTUSgen.ipynb') # default case
