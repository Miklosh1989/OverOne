from collections import Counter

with open("in.txt", 'r', encoding="utf8") as file:
    readText = file.read()
    text = readText.split(" ")
    counter = Counter(text)

with open("out.txt", 'w', encoding="utf8") as file:
    for key, val in counter.items():
        file.write('{}:{}\n'.format(key, val))








