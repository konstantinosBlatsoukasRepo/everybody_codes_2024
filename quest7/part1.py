# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///


from collections import defaultdict
import collections

from rich import print

TEST_PART1 = """A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+"""


PART1 = """I:=,+,+,-,-,+,=,+,-,=
K:+,+,+,=,=,-,-,=,+,-
E:+,=,-,+,+,-,-,=,+,=
G:+,-,+,-,=,+,=,-,=,+
H:-,=,=,-,+,+,+,-,=,+
C:-,+,-,+,+,=,+,=,=,-
F:=,+,+,-,+,+,=,-,-,=
A:=,+,+,-,-,-,=,+,=,+
B:=,+,=,+,-,+,-,-,=,+"""


def parse(input):
    parsed_input = collections.defaultdict(list)
    for line in input.splitlines():
        segment, actions = line.split(":")
        parsed_input[segment] = actions.split(",")
    return parsed_input


def solve_part_one(parsed_input, total_segments=10, initial_power=10):
    index = 0
    device_power = defaultdict(list)
    for segment in range(total_segments):
        for k, v in parsed_input.items():
            device_index = index % len(v)
            current_action = v[device_index]

            current_value = initial_power if k not in device_power else device_power[k][-1]

            match current_action:
                case "+":
                    device_power[k].append(current_value + 1)
                case "-":
                    device_power[k].append(current_value - 1)
                case "=":
                    device_power[k].append(current_value)
        index += 1

    res = sorted([(k, sum(v)) for k, v in device_power.items()], key=lambda x: x[1], reverse=True)

    return "".join([a for a, b in res])


test_parsed_part1 = parse(TEST_PART1)
print(solve_part_one(test_parsed_part1))


parsed_part1 = parse(PART1)
print(solve_part_one(parsed_part1))
