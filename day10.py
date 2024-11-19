import os

def load_file_lines(filename, base_path="Inputs/Day10/"):
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'r') as file:
        return file.read().splitlines()

file_lines = load_file_lines("everybody_codes_q10_p1.txt")

filtered_words = [line[2:6] for line in file_lines if '*' in line]

collected_letters = ''.join([word[i] for i in range(len(filtered_words[0])) for word in filtered_words])

lines_with_dots = [line for line in file_lines if '.' in line]

result_word = ''
for line in lines_with_dots:
    for letter in collected_letters:
        if letter in line:
            result_word += letter

print("What runic word will be formed upon solving your sample grid?")
print(result_word)
