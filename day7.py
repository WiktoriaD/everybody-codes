def load_file_lines(filename):
    with open(r"Inputs\Day7\\" + filename, 'r') as file_handler:
        return file_handler.read().splitlines()

def convert_input_to_dict(data, segments=10):
    plans = {}
    for line in data:
        key, value = line.split(":")
        plans[key] = value.split(",")
    for key, value in plans.items():
        if len(value) < segments:
            repeats = (segments // len(value)) + 1
            extended_value = (value * repeats)[:segments]
            plans[key] = extended_value
    return plans


def calculated_plans(dictionary, initial_power=10):
    results = {}
    for key, value in dictionary.items():
        power = initial_power
        total_power = 0
        for action in value:
            if action == "+":
                power += 1
            elif action == "-":
                power -= 1
            total_power += power
        results[key] = total_power
    return results


data = load_file_lines("everybody_codes_q07_p1.txt")
plans = convert_input_to_dict(data)
outcome = calculated_plans(plans)
sorted_outcome = sorted(outcome.items(), key=lambda x: x[1], reverse=True)

sorted_plans = ''.join([plan for plan, _ in sorted_outcome])
print("What is the ranking of the squires' action plans after 10 segments?")
print(sorted_plans)
