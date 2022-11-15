import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
names = os.path.join(ROOT_DIR, os.path.join(ROOT_DIR, 'input/Names/invited_names.txt'))
letter = os.path.join(ROOT_DIR, os.path.join(ROOT_DIR, 'input/Letters/starting_letter.txt'))


with open(letter) as read_letter:
    letter = read_letter.read()

with open(names) as read_names:
    names = list(read_names.read().split('\n'))


for name in names:
    new_letter = letter.replace('[name]', name)
    print(new_letter)
    with open(os.path.join(ROOT_DIR, f'Output/ReadyToSend/letter_for_{name}.txt'), mode="w") as completed_letter:
        completed_letter.write(new_letter)

print(names)




