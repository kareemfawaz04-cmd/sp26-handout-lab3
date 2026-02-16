"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
import pandas as pd
from src.q1 import SpamReader


class tests(unittest.TestCase):

    def test_init_2failures(self)->None:
        df = pd.DataFrame({"v4": ["ham", "spam"], "v5": ["hello", "buy now"]})
        with self.assertRaises(ValueError):
            SpamReader(df)

    def test_init_1failure(self)->None:
        with self.assertRaises(ValueError):
            SpamReader(pd.DataFrame({"v1": ["ham", "spam"], "v5": ["hello", "buy now"]}))

    def test_init_correct(self)->None:
        self.assertTrue(SpamReader(pd.DataFrame({"v1": ["ham", "spam"], "v2": ["hello", "buy now"]})).df.equals( pd.DataFrame({"v1": ["ham", "spam"], "v2": ["hello", "buy now"]})))
        
    def test_dictionary_basic(self)->None:
        df=pd.DataFrame({"v1": ["ham", "spam"], "v2": ["hello world", "buy now"]})
        self.assertEqual(SpamReader(df).get_dictionary(), {"hello", "world", "buy", "now"})

    def test_dictionary_empty(self)->None:
        df=pd.DataFrame({"v1": ["ham", "spam"], "v2": ["", ""]})
        self.assertEqual(SpamReader(df).get_dictionary(), set())

    def test_dictionary_duplicates(self)->None:
        df=pd.DataFrame({"v1": ["ham", "spam"], "v2": ["hello hello world", "buy buy now"]})
        self.assertEqual(SpamReader(df).get_dictionary(), {"hello", "world", "buy", "now"})

    def test_dictionary_mixed(self)->None:
        df=pd.DataFrame({"v1": ["ham", "spam"], "v2": ["hello world", "hello buy now"]})
        self.assertEqual(SpamReader(df).get_dictionary(), {"hello", "world", "buy", "now"})

    