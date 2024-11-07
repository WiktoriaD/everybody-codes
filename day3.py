import numpy as np


def load_input(filename):
    with open(r"Inputs\Day3\\" + filename, 'r') as file_handler:
        lines = file_handler.read().splitlines()
        return lines


def converter(filename):
    file_content = load_input(filename)
    array = np.array([[1 if char == '#' else 0 for char in line] for line in file_content])
    return array


def check_four_directions(data, i, j, layer):
    return ((data[i - 1, j] == layer or data[i - 1, j] == layer + 1) and  # Up
            (data[i + 1, j] == layer or data[i + 1, j] == layer + 1) and  # Down
            (data[i, j - 1] == layer or data[i, j - 1] == layer + 1) and  # Left
            (data[i, j + 1] == layer or data[i, j + 1] == layer + 1))    # Right


def check_diagonal_directions(data, i, j, layer):
    # Check diagonal directions (Up-left, Down-right, Up-right, Down-left)
    return ((data[i - 1, j - 1] == layer or data[i - 1, j - 1] == layer + 1) and  # Up-left
            (data[i + 1, j + 1] == layer or data[i + 1, j + 1] == layer + 1) and  # Down-right
            (data[i - 1, j + 1] == layer or data[i - 1, j + 1] == layer + 1) and  # Up-right
            (data[i + 1, j - 1] == layer or data[i + 1, j - 1] == layer + 1))    # Down-left


def digging(data, part):
    rows, columns = data.shape
    layer = 1
    while True:
        changes = False
        for i in range(1, rows - 1):
            for j in range(1, columns - 1):
                if data[i, j] == layer:
                    # Check for part 1 and 2: normal four-direction check
                    if part < 3 and check_four_directions(data, i, j, layer):
                        data[i, j] = layer + 1
                        changes = True
                    # Check for part 3: four-direction + diagonal directions
                    if part == 3 and check_four_directions(data, i, j, layer) and check_diagonal_directions(data, i, j, layer):
                        data[i, j] = layer + 1
                        changes = True

        if not changes:
            break  # If no changes were made, we stop the iteration
        layer += 1  # Move to the next layer


data = converter('everybody_codes_q3_p1.txt')
digging(data, 1)
data_2 = converter('everybody_codes_q3_p2.txt')
digging(data_2, 2)
data_3 = converter('everybody_codes_q3_p3.txt')
digging(data_3, 3)
print("How many earth blocks can be safely removed at most from your final map while maintaining the proper slope?")
print("Part I:", np.sum(data))
print("Part II:", np.sum(data_2))
print("Part III:", np.sum(data_3))
