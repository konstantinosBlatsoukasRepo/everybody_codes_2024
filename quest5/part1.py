# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///


from rich import print
from collections import defaultdict


TEST_INPUT = """2 3 4 5
3 4 5 2
4 5 2 3
5 2 3 4"""

PART1_INPUT = """3 2 4 5
3 2 3 5
4 4 5 5
2 5 4 2
4 3 3 2"""


PART2_INPUT = """42 51 61 64
36 24 26 51
42 60 82 30
21 12 45 88
56 90 53 77
37 85 74 61
30 49 58 75
43 80 27 41
22 15 56 96
93 77 25 28
46 27 13 11
48 82 48 24
35 76 41 35
69 24 57 91
71 19 56 37
35 12 29 70
16 54 38 26
19 86 75 81
55 39 19 78
15 70 17 98
15 90 44 83
51 62 35 74
46 69 76 72
61 93 69 38
31 17 63 53
28 20 40 75
89 87 41 71
41 59 65 73
66 72 22 18
90 33 84 31
99 43 11 35
18 25 22 43
93 10 62 36
14 50 81 78
53 70 27 91
15 33 40 79
85 47 17 33
32 17 97 10
61 95 33 21
54 76 93 27
34 40 50 43
44 86 97 86
44 72 14 24
98 26 60 36
95 31 67 23
80 81 82 38
73 34 95 44
96 48 38 85
59 79 68 29
28 85 79 89
80 28 88 92
55 89 23 83
20 31 74 11
23 55 67 63
42 55 36 13
34 11 83 25
13 33 53 14
94 65 63 99
46 88 94 37
65 42 87 68
81 28 43 94
66 86 14 60
22 49 98 46
19 65 82 15
90 69 79 99
32 13 25 41
64 39 94 20
92 12 87 21
39 62 51 39
97 89 12 58
10 42 11 73
98 31 52 49
75 56 60 50
49 18 24 44
32 40 97 77
23 27 71 16
67 57 12 88
73 58 96 70
67 66 37 52
64 96 32 45
77 16 62 39
48 84 57 78
54 25 68 66
72 29 45 84
34 36 26 59
26 20 16 83
80 63 74 54
45 32 17 47
57 20 78 91
64 19 30 13
14 68 99 92
34 30 29 29
30 18 50 87
92 52 10 47
46 58 37 91
40 71 21 47
16 95 38 18
84 76 52 21
23 59 45 22"""


def parse(input):
    all_lines = input.splitlines()

    columns = [[] for _ in range(len(all_lines[0].split(" ")))]

    for line in all_lines:
        for index, val in enumerate(line.split(" ")):
            columns[index].append(int(val))

    return columns


def start_dance(parsed_input: int, rounds: int):
    current_column_clapper_index = 0
    for round in range(rounds):
        current_column_clapper_index = current_column_clapper_index % (len(parsed_input))

        target_column = (current_column_clapper_index + 1) % len(parsed_input)

        current_first_clapper = parsed_input[current_column_clapper_index].pop(0)

        # "bounce" reflection indexing
        n = len(parsed_input[target_column])
        pos = (current_first_clapper - 1) % (2 * n)

        idx = pos if pos < n else 2 * n - pos

        parsed_input[target_column].insert(idx, current_first_clapper)

        current_column_clapper_index += 1

        print(f"round {round + 1}: {''.join([str(ele[0]) for ele in parsed_input])}")


parsed_input = parse(PART1_INPUT)

start_dance(parsed_input, 11)


def start_dance_part2(parsed_input: int):
    current_column_clapper_index = 0

    freq = defaultdict(int)
    num_found = 0

    round = 1
    while True:
        current_column_clapper_index = current_column_clapper_index % (len(parsed_input))

        target_column = (current_column_clapper_index + 1) % len(parsed_input)

        current_first_clapper = parsed_input[current_column_clapper_index].pop(0)

        # "bounce" reflection indexing
        n = len(parsed_input[target_column])
        pos = (current_first_clapper - 1) % (2 * n)

        idx = pos if pos < n else 2 * n - pos

        parsed_input[target_column].insert(idx, current_first_clapper)

        current_column_clapper_index += 1

        shouted_num = "".join([str(ele[0]) for ele in parsed_input])
        freq[shouted_num] += 1

        if freq[shouted_num] == 2024:
            num_found = shouted_num
            break

        round += 1

    print(int(num_found) * round)
    return int(num_found) * round


TEST_PART2_INPUT = """2 3 4 5
6 7 8 9"""

test_parsed_input = parse(TEST_PART2_INPUT)

assert start_dance_part2(test_parsed_input) == 50877075

parsed_input_part_tow = parse(PART2_INPUT)

print(start_dance_part2(parsed_input_part_tow))


def start_dance_part3(parsed_input: int):
    current_column_clapper_index = 0

    seen_nums = set()
    round = 1

    freq = defaultdict(int)

    while True:
        current_column_clapper_index = current_column_clapper_index % (len(parsed_input))

        target_column = (current_column_clapper_index + 1) % len(parsed_input)

        current_first_clapper = parsed_input[current_column_clapper_index].pop(0)

        # "bounce" reflection indexing
        n = len(parsed_input[target_column])
        pos = (current_first_clapper - 1) % (2 * n)

        idx = pos if pos < n else 2 * n - pos

        parsed_input[target_column].insert(idx, current_first_clapper)

        current_column_clapper_index += 1

        shouted_num = "".join([str(ele[0]) for ele in parsed_input])

        shouted_num = "".join([str(ele[0]) for ele in parsed_input])
        freq[shouted_num] += 1

        if freq[shouted_num] == 2024:
            break

        seen_nums.add(int(shouted_num))
        round += 1

    return max(seen_nums)


TEST_PART3_INPUT = """2 3 4 5
6 7 8 9"""

test_parsed_input = parse(TEST_PART3_INPUT)

assert start_dance_part3(test_parsed_input) == 6584



PART3_INPUT = """1005 1006 1003 1009
1003 1004 1006 1004
1004 1004 1004 1004
1001 1000 1000 1005
1003 1001 1006 6147
1005 1008 1009 1007
1000 1006 1004 1006
1009 1003 1003 3341
1000 1009 1005 9912
1001 1000 1002 1003
1000 9624 1002 1005
1005 1002 1000 1001
1007 1009 1008 1000
1006 1008 1007 1006
1008 1003 1006 1001
1004 1006 1001 5149
1005 1009 1008 1009
1004 1003 8690 1000
1001 2605 6100 1006
1003 1002 1001 7403
1005 1004 1004 1006
2294 1007 1006 1002
1004 1001 1007 1005
1008 1009 1007 1002
1003 1003 1001 2206
1004 1002 1002 1008
1006 1002 1003 1001
1007 8045 1006 1005
1000 1001 1001 1008
1004 1001 1008 1007
1001 1009 1000 1005
1000 1005 1009 1003
1002 1001 1001 1003
5565 1002 4332 1007
1001 1004 1001 1001
1000 1004 1005 1002
8384 1008 1000 1001
1000 1004 5998 1000
1008 1009 1003 1005
1004 1008 1001 1003
1000 1009 6452 1000
1000 1001 1004 1009
1007 9086 1004 1000
1001 1007 1003 1005
1007 1005 1006 1007
1000 8201 1004 1001
1006 1001 1000 1007
1006 1003 1003 1004
1005 1006 1008 6426
1003 1007 1005 1007"""


parsed_input = parse(PART3_INPUT)


print(start_dance_part3(parsed_input))