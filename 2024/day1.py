potions = 0
additional_potions = 0


def load_input(filename):
    with (open(r"Inputs\Day1\\" + filename) as
          file_handler):
        file = file_handler.read()
        return file


def potions_count(letter):
    global potions
    if letter == 'B':
        potions += 1
    elif letter == 'C':
        potions += 3
    elif letter == 'D':
        potions += 5
    return potions


def additional_potions_count(group):
    global additional_potions
    x_count = group.count('x')
    if x_count == 1 and len(group) == 3:
        additional_potions += 2
    elif x_count == 0 and len(group) == 3:
        additional_potions += 6
    elif x_count == 0 and len(group) == 2:
        additional_potions += 2
    else:
        additional_potions += 0


def count_basic_potion(file):
    return [potions_count(char) for char in file]


def count_extra_potions(file, how_many_monsters):
    monster_groups = [file[i:i+how_many_monsters] for i in range(0, len(file), how_many_monsters)]
    for monster in monster_groups:
        additional_potions_count(monster)
    return additional_potions


def outcome():
    global potions
    global additional_potions
    result = potions + additional_potions
    potions = 0
    additional_potions = 0
    return result

print("What is the exact number of potions that need to be prepared for your battle?")
data_part1 = load_input('everybody_codes_p1.txt')
basic_part1 = count_basic_potion(data_part1)
print(outcome())

print("What is the exact number of potions you need to order for round two?")
data_part2 = load_input('everybody_codes_p2.txt')
basic_part2 = count_basic_potion(data_part2)
extras_part2 = count_extra_potions(data_part2, 2)
print(outcome())

print("What is the exact number of potions you need to order for the final round?")
data_part3 = load_input('everybody_codes_p3.txt')
basic_part3 = count_basic_potion(data_part3)
extras_part3 = count_extra_potions(data_part3, 3)
print(outcome())
