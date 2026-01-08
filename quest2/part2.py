TEST_INPUT = """WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ"""


def parse(input):
    lines = input.splitlines()
    words = lines[0].split(":")[1].split(",")
    reversed_words = [word[::-1] for word in words]
    words.extend(reversed_words)
    inscription_lines = lines[2:]
    return words, inscription_lines


def count_runic_symbols(words, inscription_word):
    count = set()
    for word in words:
        for i, val in enumerate(inscription_word):
            if i + len(word) > len(inscription_word):
                break
            if inscription_word[i : i + len(word)] == word:
                count |= set(range(i, i + len(word)))

    return len(count)


assert count_runic_symbols(["QAQ"], "QAQAQ") == 5
assert count_runic_symbols(["THE"], "THE") == 3


def count_runic_symbols_in_a_line(words, inscription_line):
    total = 0
    for inscription_word in inscription_line.split():
        total += count_runic_symbols(words, inscription_word)
    return total


test_words, test_lines = parse(TEST_INPUT)
# print(test_lines)

assert count_runic_symbols_in_a_line(test_words, "AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE") == 15
assert count_runic_symbols_in_a_line(test_words, "THE FLAME SHIELDED THE HEART OF THE KINGS") == 9
assert count_runic_symbols_in_a_line(test_words, "POWE PO WER P OWE R") == 6
assert count_runic_symbols_in_a_line(test_words, "THERE IS THE END") == 7
assert count_runic_symbols_in_a_line(test_words, "QAQAQ") == 5


def part2(input):
    words, inscription_lines = parse(input)
    total_runic_symbols = 0
    for inscription_line in inscription_lines:
        total_runic_symbols += count_runic_symbols_in_a_line(words, inscription_line)
    return total_runic_symbols


assert part2(TEST_INPUT) == 42

with open("input_part2.txt") as f:
    INPUT = f.read()

print(part2(INPUT))

# import timeit
# print(timeit.timeit("count_runic_symbols(['QAQ'], 'QAQAQ')", globals=globals()))
