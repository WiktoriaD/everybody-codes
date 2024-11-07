import re


def load_input(filename):
    with (open(r"Inputs\Day2\\" + filename) as
          file_handler):
        file = file_handler.readlines()
        return file


def converter(data):
    pattern = data[0][6:].replace(',', '|').strip()
    text = data[2]
    print(pattern)
    print(text)
    return pattern, text


def count_words(pattern, text):
    start = 0
    matches = []

    while start < len(text):
        match = re.search(pattern, text[start:], re.IGNORECASE)
        if match:
            matches.append(match.group())
            start += match.start() + 1
        else:
            break

    print("Number of matches:", len(matches))

data = load_input('everybody_codes_q2_p1.txt')
pattern, text = converter(data)
count_words(pattern, text)
