TEST_INPUT = """WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"""

INPUT = """WORDS:LOR,LL,SI,OR,GI,AG,OL

LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT. DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM."""

def parse(input):
    lines = input.splitlines()
    words = lines[0].split(":")[1].split(",")
    inscription_words = lines[2].split()
    return words, inscription_words


def count_runic_words(input):
    words, inscription_words = parse(input)

    total_runic_words = 0
    for inscription_word in inscription_words:
        for word in words:
            if word in inscription_word:
                total_runic_words += 1

    return total_runic_words


count_runic_words(TEST_INPUT) == 4

print(count_runic_words(TEST_INPUT))

print(count_runic_words(INPUT))