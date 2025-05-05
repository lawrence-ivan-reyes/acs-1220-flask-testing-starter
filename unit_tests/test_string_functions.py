from unittest import TestCase

from .string_functions import *

class StringTests(TestCase):
    def test_greeting_jeremy(self):
        """Test for greet_by_name"""
        # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

        # Step 2: Decide what the expected outcome is for the scenario
        expected = 'Hello, Jeremy!'

        # Step 3: Call the function being tested to get its actual output
        actual = greet_by_name('Jeremy')

        # Step 4: Compare expected & actual outcomes. If they match, the test 
        # passes
        self.assertEqual(actual, expected)

    def test_greeting_dani(self):
        """Test for greet_by_name"""
        expected = 'Hello, Dani!'
        actual = greet_by_name('Dani')
        self.assertEqual(actual, expected)

    def test_greeting_empty(self):
        """Test for greet_by_name with an empty name."""
        expected = 'Hello, !'
        actual = greet_by_name('')
        self.assertEqual(actual, expected)

    def test_reverse_long(self):
        """Test reversing a long string."""
        expected = 'nohtyP evol I'
        actual = reverse('I love Python')
        self.assertEqual(actual, expected)

    def test_reverse_short(self):
        """Test reversing a short string."""
        expected = 'olleH'
        actual = reverse('Hello')
        self.assertEqual(actual, expected)

    def test_reverse_empty(self):
        """Test reversing an empty string."""
        expected = ''
        actual = reverse('')
        self.assertEqual(actual, expected)

    def test_reverse_with_special_chars(self):
        """Test reversing a string with special characters."""
        expected = '!@#$ olleH'
        actual = reverse('Hello $#@!')
        self.assertEqual(actual, expected)

    def test_reverse_words_long(self):
        """Test reversing words in a long string."""
        expected = 'I evol nohtyP gnimmargorp'
        actual = reverse_words('I love Python programming')
        self.assertEqual(actual, expected)

    def test_reverse_words_short(self):
        """Test reversing words in a short string."""
        expected = 'olleH dlroW'
        actual = reverse_words('Hello World')
        self.assertEqual(actual, expected)

    def test_reverse_words_empty(self):
        """Test reversing words in an empty string."""
        expected = ''
        actual = reverse_words('')
        self.assertEqual(actual, expected)

    def test_reverse_words_single_word(self):
        """Test reversing a single word."""
        expected = 'olleH'
        actual = reverse_words('Hello')
        self.assertEqual(actual, expected)

    def test_sarcastic_long(self):
        """Test sarcastic-ifying a long string."""
        expected = 'ThIs Is A lOnG sTrInG fOr TeStInG'
        actual = sarcastic('This is a long string for testing')
        self.assertEqual(actual, expected)

    def test_sarcastic_short(self):
        """Test sarcastic-ifying a short string."""
        expected = 'HeY tHeRe'
        actual = sarcastic('Hey there')
        self.assertEqual(actual, expected)

    def test_sarcastic_empty(self):
        """Test sarcastic-ifying an empty string."""
        expected = ''
        actual = sarcastic('')
        self.assertEqual(actual, expected)

    def test_sarcastic_with_numbers(self):
        """Test sarcastic-ifying a string with numbers and punctuation."""
        expected = 'HeLlO 123 wOrLd!'
        actual = sarcastic('Hello 123 World!')
        self.assertEqual(actual, expected)

    def test_find_longest_word_empty(self):
        """Test finding the longest word in an empty sentence."""
        result = find_longest_word('')
        self.assertEqual(result, "")

    def test_find_longest_word_tie(self):
        """Test finding the longest word when there's a tie."""
        expected = 'hello'  # should return first longest word, so hello since it comes before world
        actual = find_longest_word('hello world')
        self.assertEqual(actual, expected)
