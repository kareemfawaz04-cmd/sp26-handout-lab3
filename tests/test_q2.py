"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from unittest import mock
import pandas as pd
from src.q2 import SpamReader

# You are not required to test visualizations.
# You may ignore this file.
# This is a test being run in the autograder, if you're curious.
# It uses unittest.mock, just like how you've used it to test printed things.

class TestPlotWordFrequencies(unittest.TestCase):
    """Test for SpamReader.plot_word_frequencies"""

    @mock.patch('src.q2.plt')
    @mock.patch('src.q2.BaseSpamReader')
    def test_plot_word_frequencies(
        self, mock_base_reader_class: mock.Mock, mock_plt: mock.Mock) -> None:
        """Test that word counts are calculated and plotted correctly"""
        df = pd.DataFrame({
            'v1': ['spam', 'spam', 'ham', 'ham', 'spam'],
            'v2': ['buy now', 'buy free', 'hello there', 'buy groceries', 'free prize']
        })
        
        # Mock the get_dictionary method
        mock_base_instance = mock.Mock()
        mock_base_instance.get_dictionary.return_value = {'buy', 'free'}
        mock_base_reader_class.return_value = mock_base_instance
        
        reader = SpamReader(df)
        reader.plot_word_frequencies()
        
        # Get the call to plt.scatter
        call_args = mock_plt.scatter.call_args
        ham_counts = call_args[0][0]
        spam_counts = call_args[0][1]
        
        # 'buy': 2 times in spam ('buy now', 'buy free')
        #        1 time in ham ('buy groceries')
        # 'free': 2 times in spam ('buy free', 'free prize')
        #         0 times in ham
        # Expected: ham_counts = [1, 0], spam_counts = [2, 2]
        self.assertEqual(len(ham_counts), 2)
        self.assertEqual(len(spam_counts), 2)
        self.assertIn(1, ham_counts)
        self.assertIn(0, ham_counts)
        self.assertIn(2, spam_counts)
