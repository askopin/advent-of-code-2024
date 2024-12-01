import unittest
from day_1 import Day1
from io import StringIO

class TestTask1(unittest.TestCase):

    def test_given_sample(self):
        input = """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """
        expected_result = 11
        diff_score = Day1.task_1(StringIO(input.strip()))
        assert(diff_score == expected_result)
    
    def test_equal_scores(self):
        input = """
        1   3
        2   2
        3   1
        """
        expected_result = 5
        diff_score = Day1.task_1(StringIO(input.strip()))
        assert(diff_score == expected_result)

    def test_single_line(self):
        input = """
        1   3
        """
        expected_result = 2
        diff_score = Day1.task_1(StringIO(input.strip()))
        assert(diff_score == expected_result)    


if __name__ == "__main__":
    unittest.main()