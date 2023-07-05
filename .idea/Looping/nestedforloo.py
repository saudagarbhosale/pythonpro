'''for letter in 'saudagar':
    if letter == 'a' or letter == 'g':
        continue
    print('letters: ', letter)

for l in 'Saudagar':
    if l == 's' or l == 'd':
        break
    print("letter is: ", l)

fruit = ["apple", "mango", "banana"]

iter_obj = iter(fruit)

while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break'''

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print(letter)


