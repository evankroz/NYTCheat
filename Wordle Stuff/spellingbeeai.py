pos_list = []
answers = []
perfect_spam = []
inp = input("Please enter the letters that are present in today's nyt\n"
            "the middle letter must be the first one and capitalized: ")

with open("Texts/twl06.txt") as txt:
    for line in txt:
        if len(line) > 3:
            pos_list.append(line.strip())

while len(inp) != 7:
    print("Invalid")
    inp = input("Please enter the letters that are present in today's nyt\n"
                "the middle letter must be the first one and capitalized: ")
inp = list(inp)

short_list = sorted(pos_list, key=lambda x: len(x), reverse=True)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
unacept = [letter for letter in alphabet if letter not in inp]
pangram = []
for word in short_list:
    if inp[0] in word:
        if word not in answers:
            if len(word) > 3:
                if not any(letter in unacept for letter in word):
                    answers.append(word)

for word in answers:
    if all(letter in word for letter in inp):
        if len(set(word)) == 7:
            pangram.append(word)

print(answers)
print(f"This is the pangram: {pangram}")
