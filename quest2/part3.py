# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///

from rich import print

TEST_INPUT = """WORDS:THE,OWE,MES,ROD,RODEO

HELWORLT
ENIGWDXL
TRODEOAL"""


def part3(input):
    text = input.splitlines()

    words = text[0].split(":")[1].split(",")

    lines = [val for val in text[2:]]

    scales = set()
    for word in words:
        rev_word = word[::-1]
        for i in range(len(lines)):
            row_base = lines[i]
            row_ext = row_base + row_base[: len(word) - 1]
            for j in range(len(row_ext)):
                if row_ext[j:].startswith(word) or row_ext[j:].startswith(rev_word):
                    for k in range(j, j + len(word)):
                        scales.add((i, k % len(row_base)))
        for j in range(len(lines[0])):
            column = "".join([lines[x][j] for x in range(len(lines))])
            for i in range(len(column)):
                if column[i:].startswith(word) or column[i:].startswith(rev_word):
                    for k in range(i, i + len(word)):
                        scales.add((k, j))

    print(len(scales))


part3(TEST_INPUT)


with open("input_part3.txt") as f:
    part3(f.read())