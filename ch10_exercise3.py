name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')
text = handle.read()
text = text.lower()
freq = {}

for letter in text:
    if letter.isalpha():
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

sortletter = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for letter, count in sortletter:
    print(letter, count)

