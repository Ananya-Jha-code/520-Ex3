import unittest
from src.solution import split_words

class TestSplitWordsSpec(unittest.TestCase):

    # 1. If txt contains a space → result must be a list
    def test_result_is_list_when_space_present(self):
        res = split_words("a b c")
        self.assertIsInstance(res, list)

    # 2. If txt contains a comma and no space → result must be a list
    def test_result_is_list_when_comma_and_no_space(self):
        res = split_words("x,y,z")
        self.assertIsInstance(res, list)

    # 3. If txt contains a space → len(res) == len(txt.split())
    def test_result_length_matches_whitespace_split(self):
        txt = "hello   world   test"
        res = split_words(txt)
        self.assertEqual(len(res), len(txt.split()))

    # 4. If no space and no comma → result must be an integer
    def test_result_is_int_when_no_space_no_comma(self):
        res = split_words("abcdef")
        self.assertIsInstance(res, int)

    # 5. If no space/comma → result equals lowercase odd-index count
    def test_odd_index_lowercase_count(self):
        txt = "a1b2c3d"
        expected = sum(
            1 for c in txt
            if c.islower() and ((ord(c) - ord('a')) % 2 == 1)
        )
        res = split_words(txt)
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
