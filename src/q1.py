"""
We will use the same dataset as last time, spam.csv.
The original dataset is available at 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Please ignore the rows that do not follow the correct format.

This problem is to help you practice writing tests. To save you time, 
we have provided the code for the SpamReader class and its methods 
below. Your task, for this problem, is to write the tests in test_q1.py.
"""

import sys
sys.path.append(".")
import pandas as pd

class SpamReader:
    """A class to get the dictionary of words from a spam dataset."""
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Store the provided dataframe.

        Args:
            df (pd.DataFrame): A dataframe containing the spam dataset.
        
        Raises:
            ValueError: If the dataframe does not contain the columns 'v1' and 'v2'
        """
        if 'v1' not in df.columns or 'v2' not in df.columns:
            raise ValueError("DataFrame must contain 'v1' and 'v2' columns")
        self.df = df

    def get_dictionary(self) -> set[str]:
        """
        Return a set of all words that appear in the messages.
        
        Returns:
            set[str]: A set of all words that appear in the messages.
        """
        words = set()
        for message in self.df['v2']:
            words.update(message.split())
        return words