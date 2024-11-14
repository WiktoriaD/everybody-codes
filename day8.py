def load_file(filename):
    with open(r"Inputs\Day8\\" + filename, 'r') as file_handler:
        return file_handler.read()


def solve_quest_1(available_blocks):
    blocks = int(available_blocks) - 1
    foundations = 1
    height = 1

    while blocks > 0:
        foundations += 2
        if blocks - foundations > 0:
            blocks -= foundations
        else:
            additional_blocks = foundations - blocks
            blocks = 0
        height += 1
    return (height * 2 - 1) * additional_blocks


def solve_quest_2():
    foundations = 1
    thickness = 1
    last_layer_blocks = 0
    remaining_blocks = 20240000
    PRIESTS = 815
    ACOLYTES = 1111
    total_blocks_used = 0

    while remaining_blocks > 0:
        last_layer_blocks = thickness * foundations
        if remaining_blocks >= last_layer_blocks:
            remaining_blocks -= last_layer_blocks
            total_blocks_used += last_layer_blocks
            foundations += 2
            thickness = (thickness * PRIESTS) % ACOLYTES
        else:
            break

    additional_blocks_needed = last_layer_blocks - remaining_blocks
    return additional_blocks_needed * foundations


print("""Part I
Determine the final width of the shrine and the number of additional blocks needed to complete the final layer.
What is the result of multiplying the number of missing blocks by the target width?""")
file = load_file("everybody_codes_q08_p1.txt")
print(solve_quest_1(file))

print("""Part II
Determine the final width of the shrine and the number of additional blocks needed to complete the last layer.
What do you get if you multiply these two numbers?""")
print(solve_quest_2())
