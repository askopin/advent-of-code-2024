from typing import List, Tuple, TextIO

class Day1:
    def parse_data(input: TextIO) -> Tuple[List[int], List[int]]:
        left_list, right_list = list(zip(*(line.strip().split('   ') for line in input.readlines())))
        left_list = [int(x) for x in left_list]
        right_list = [int(x) for x in right_list]
        return left_list, right_list

    def task_1(input: TextIO) -> int:
        left_list, right_list = Day1.parse_data(input)
        left_list.sort()
        right_list.sort()
        diff_score = sum([abs(line[0] - line[1]) for line in zip(left_list, right_list)])
        return diff_score

if __name__ == '__main__':
    with open('input_1.txt', 'r') as f:
        print(f"differense score: {Day1.task_1(f)}")
