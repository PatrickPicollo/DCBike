"""
IE DC Bike Utils.
"""

__version__ = "0.1.0"

import pandas as pd

def tokenize(text):
    return text.split()

if __name__ == "__main__":
    print(tokenize("Hello World"))