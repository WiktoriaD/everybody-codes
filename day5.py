def load_file_lines(filename):
    with open(r"Inputs\Day5\\" + filename, 'r') as file_handler:
        return file_handler.read().splitlines()


def convert_lines_to_array(filename):
    lines = load_file_lines(filename)
    data = [list(map(int, column)) for column in zip(*[line.split() for line in lines])]
    return data


def run_dance_simulation(file_data, num_rounds):
    for dance_round in range(num_rounds):
        print(f"Round {dance_round + 1}: ", end="")
        print("Before", file_data)
        current_column = dance_round % len(file_data)
        clapper = file_data[current_column][0]
        target_column = (current_column + 1) % len(file_data)

        # Extract the length of the target column into a variable
        target_column_len = len(file_data[target_column])

        file_data[current_column].pop(0)

        # Use the extracted target column length in the new index calculation
        if clapper <= target_column_len:
            index = clapper - 1
        else:
            index = abs(clapper - target_column_len) - 1

        file_data[target_column].insert(index, clapper)

        combined_number = int("".join(str(file_data[col][0]) for col in range(len(file_data))))
        print(f"After {file_data}")
        print(f"{combined_number}")


file_data = convert_lines_to_array("everybody_codes_q5_p1.txt")
num_rounds = int(input("How many rounds of The Clapper dance? "))
run_dance_simulation(file_data, num_rounds)
