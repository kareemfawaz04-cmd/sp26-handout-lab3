"""
We will use the same dataset as last time, spam.csv.
The original dataset is available at 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Please ignore the rows that do not follow the correct format.

Implement this class to analyze the data according to the documentation.

Make sure to also write tests for it.
"""

import sys
sys.path.append(".")
import pandas as pd

class SpamSorter:
    """A class to sort messages by the frequency of a given word."""
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Store the provided dataframe.

        Args:
            df (pd.DataFrame): A dataframe containing the spam dataset.
        
        Raises:
            ValueError: If the dataframe does not contain the columns 'v1' and 'v2'
        """
        # The constructor is provided to you
        if 'v1' not in df.columns or 'v2' not in df.columns:
            raise ValueError("DataFrame must contain 'v1' and 'v2' columns")
        self.df = df

    def sort_by_word_frequency(
            self, word: str, include_spam: bool = True, include_ham: bool = True) -> list[str]:
        """
        Return a list of the SMS messages, sorted by the number of times that the given
        word appears in the message. The messages in which the word appears most often
        is first. If there is a tie, either message can be first. Case sensitive.

        If include_spam is False, filter out all of the spam in the resulting list.
        If include_ham is False, filter out all of the ham in the resulting list.

        Args:
            word (str): The word to count in each message.
            include_spam (bool): Whether to include spam messages in the result.
            include_ham (bool): Whether to include ham messages in the result.
        
        Returns:
            list[str]: A list of messages  sorted by the frequency of the given word.
        """

        list_of_messages = []

        for _, row in self.df.iterrows():
            label = row["v1"]

            if label == "spam" and not include_spam:
                continue
            if label == "ham" and not include_ham:
                continue

            message = row["v2"]
            count = message.count(word)

            list_of_messages.append((count, message))

        list_of_messages.sort(reverse=True)

        return [msg for _, msg in list_of_messages]


