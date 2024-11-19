def load_file(filename):
    with open(r"Inputs\Day9\\" + filename, 'r') as file_handler:
        return file_handler.read().splitlines()


def count_beetles(lines):
    stamps = [10, 5, 3, 1]
    total_beetles = 0
    for value in lines:
        value = int(value)
        remaining = value
        for stamp in stamps:
            total_beetles += remaining // stamp
            remaining %= stamp
    return total_beetles

list_of_brightnesses = load_file("everybody_codes_q09_p1.txt")
print("What is the minimum number of beetles you need to stamp to construct all sparkballs from the list?"
      f"\n{count_beetles(list_of_brightnesses)}")
