"""Tests for Lab 1 Question 3"""
import sys
sys.path.append(".")
import unittest
import pandas as pd
from src.q3 import SpamSorter


class TestSortByWordFrequency(unittest.TestCase):

    def setUp(self) -> None:
        self.df = pd.DataFrame({
            "v1": ["ham", "spam", "ham", "spam"],
            "v2": [
                "buy buy now",
                "buy now",
                "hello there",
                "BUY buy"
            ]
        })
        self.sorter = SpamSorter(self.df)

    def test_basic_sorting(self) -> None:
        result = self.sorter.sort_by_word_frequency("buy")
        self.assertEqual(result[0], "buy buy now")
        self.assertEqual(set(result), set(self.df["v2"]))

    def test_filter_out_spam(self) -> None:
        result = self.sorter.sort_by_word_frequency("buy", include_spam=False)
        self.assertEqual(set(result), {"buy buy now", "hello there"})
        self.assertEqual(result[0], "buy buy now")

    def test_filter_out_ham(self) -> None:
        result = self.sorter.sort_by_word_frequency("buy", include_ham=False)
        self.assertEqual(set(result), {"buy now", "BUY buy"})

    def test_case_sensitive(self) -> None:
        result = self.sorter.sort_by_word_frequency("BUY")
        self.assertEqual(result[0], "BUY buy")

    def test_word_not_present(self) -> None:
        result = self.sorter.sort_by_word_frequency("zzz")
        self.assertEqual(set(result), set(self.df["v2"]))


if __name__ == "__main__":
    unittest.main()
