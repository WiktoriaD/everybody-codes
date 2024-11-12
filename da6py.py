def load_file_lines(filename):
    with open(r"Inputs\Day6\\" + filename, 'r') as file_handler:
        return file_handler.read().splitlines()

def find_unique_path_to_fruit(filename, first_letter_only=True):
    file = load_file_lines(filename)
    apples = []
    parents = {}
    branches = {}

    for line in file:
        parent, children = line.strip().split(":")
        for child in children.split(","):
            if child == "@":
                apples.append(parent)
            else:
                parents[child] = parent

    for apple in apples:
        current = apple
        path = ["@", apple]

        while current in parents:
            next_node = parents[current]
            if next_node in path:
                break
            current = next_node
            path.append(current)

        path_len = len(path)
        if path_len not in branches:
            branches[path_len] = []
        branches[path_len].append(path)

    powerful = next(path for paths in branches.values() if len(paths) == 1 for path in paths)

    if first_letter_only:
        return ''.join([p[0] for p in powerful[::-1]])
    else:
        return ''.join(powerful[::-1])

filename = "everybody_codes_q06_p1.txt"
result = ''.join(find_unique_path_to_fruit(filename))
unique_path_to_fruit = find_unique_path_to_fruit(filename, False)
print("Part I")
print("What is the path to the most powerful fruit on your tree?", unique_path_to_fruit)

filename_2 = "everybody_codes_q06_p2.txt"
unique_path_to_fruit_2 = find_unique_path_to_fruit(filename_2)
print("Part II")
print("What is the path to the most powerful fruit on your tree?", unique_path_to_fruit_2)

filename_3 = "everybody_codes_q06_p3.txt"
unique_path_to_fruit_3 = find_unique_path_to_fruit(filename_3)
print("Part III")
print("What is the path to the most powerful fruit on your tree?", unique_path_to_fruit_3)
