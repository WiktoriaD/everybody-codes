from collections import defaultdict

def load_file_lines(filename):
    with open(r"Inputs\Day11\\" + filename, 'r') as file:
        return file.read().splitlines()

def convert_file_to_dict(file):
    generations = {}
    for generation in file:
        key, value = generation.split(':')
        generations[key] = value.split(',')
    return generations


def solve_quest_1_2(generations, days, start_letter):
    population = start_letter
    for i in range(days):
        new_population = []
        for termite in population:
            new_population.extend(generations[termite])
        population = new_population
    return len(population)


def solve_quest_3(generations):
    by_type = {}
    for termite_type in generations.keys():
        populations = {termite_type: 1}
        for day in range(20):
            new_populations = defaultdict(int)
            for key, value in populations.items():
                for next_termite in generations[key]:
                    new_populations[next_termite] += value
            populations = new_populations
        by_type[termite_type] = sum(populations.values())

    smallest_num = min(by_type.values())
    max_num = max(by_type.values())
    return max_num - smallest_num

file_1 = load_file_lines("everybody_codes_q11_p1.txt")
generations_1 = convert_file_to_dict(file_1)
solve_quest_1 = solve_quest_1_2(generations_1, 4, 'A')
print("Part I")
print(f"What will be the termite population count on the 4th day? {solve_quest_1}")

file_2 = load_file_lines("everybody_codes_q11_p2.txt")
generations_2 = convert_file_to_dict(file_2)
solve_quest_2 = solve_quest_1_2(generations_2, 10, 'Z')
print("Part II")
print(f"What will be the termite population count on the 10th day? {solve_quest_2}")

file_3 = load_file_lines("everybody_codes_q11_p3.txt")
generations_3 = convert_file_to_dict(file_3)
solve_quest_3 = solve_quest_3(generations_3)
print("Part III")
print(f"What is the population difference on the 20th day? {solve_quest_3}")
