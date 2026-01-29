"""
We will use the same dataset as last time, spam.csv.
The original dataset is available at 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Please ignore the rows that do not follow the correct format.

Implement this class to analyze the data according to the documentation.
"""

import sys
sys.path.append(".")
import pandas as pd
import matplotlib.pyplot as plt

class SpamReader:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Store the provided dataframe.

        Args:
            df (pd.DataFrame): A dataframe containing the spam dataset.
        
        Raises:
            ValueError: If the dataframe does not contain the columns 'v1' and 'v2'
        """
        self.df = df

    def plot_word_frequencies(self) -> None:
        """
        For each word in the dictionary (from get_dictionary()), count the number of times
        that it appears in spam, and the number of times that it appears in ham.
        Plot it with ham on the x axis and spam on the y axis.
        """
        pass
