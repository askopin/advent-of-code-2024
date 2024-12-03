from typing import List, Tuple, TextIO
from math import sig

class Day2:
    def parse_data(input: TextIO) -> List[List[int]]:
        lines = (line.strip().split() for line in input.readlines())
        lines = [[int(x) for x in line] for line in lines]
        return lines
    
    # this is not the optimal solution fron the performance perspective
    # but it is the most readable one
    def is_line_safe(line: List[int]) -> bool:
        # make a list of differences between the elements
        diffs = [line[i: i+1] for i in range(len(line) - 1)]

        # check if all the elements have the same sign
        # if any of the differences is 0 (aka we have to equal values), then the line is not safe
        if not all(x * diffs[0] > 0 for x in diffs):
            return False
        
        # check if adjusted levels differ by at most three
        if not all(abs(x) <= 3 for x in diffs):
            return False

        return True

    # def task_1(input: TextIO) -> int:
    #     left_list, right_list = Day1.parse_data(input)
    #     left_list.sort()
    #     right_list.sort()
    #     diff_score = sum([abs(line[0] - line[1]) for line in zip(left_list, right_list)])
    #     return diff_score

    # def task_2(input: TextIO) -> int:
    #     left_list, right_list = Day1.parse_data(input)
    #     right_map = defaultdict(lambda: 0)
    #     for value in right_list:
    #         right_map[value] += 1
        
    #     similarity_score = sum(l_val * right_map[l_val] for l_val in left_list)
    #     return similarity_score
    
if __name__ == '__main__':
    with open('input_test.txt', 'r') as f:
        print(Day2.parse_data(f))
        # print(f"differense score: {Day1.task_1(f)}")

    # with open('input_1.txt', 'r') as f:
    #     print(f"similarity score: {Day1.task_2(f)}")