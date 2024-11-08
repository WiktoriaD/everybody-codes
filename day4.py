def load_file_lines(filename):
    with open(r"Inputs\Day4\\" + filename, 'r') as file_handler:
        return file_handler.read().splitlines()

def convert_lines_to_integers(lines):
    return sorted(list(map(int, lines)))

def calculate_total_strikes(strikes, reference_value):
    return sum(abs(strike - reference_value) for strike in strikes)


def process_part_1_2(file_name):
    file_lines = load_file_lines(file_name)
    numeric_inputs = convert_lines_to_integers(file_lines)
    min_strike = numeric_inputs[0]
    return calculate_total_strikes(numeric_inputs, min_strike)


def process_part_3(file_name):
    file_lines = load_file_lines(file_name)
    numeric_inputs = convert_lines_to_integers(file_lines)
    middle_value = numeric_inputs[len(numeric_inputs) // 2]
    return calculate_total_strikes(numeric_inputs, middle_value)


print("What is the minimum number of hammer strikes needed to level all the nails?")

print("Part I:", process_part_1_2("everybody_codes_q4_p1.txt"))

print("Part II:", process_part_1_2("everybody_codes_q4_p2.txt"))

print("Part III:", process_part_3("everybody_codes_q4_p3.txt"))
