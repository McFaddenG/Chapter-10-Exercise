name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = {}

for line in handle:
    if line.startswith("From "):
        words = line.split()
        if len(words) > 1:
            email = words[1]
            counts[email] = counts.get(email, 0) + 1

sortcount = sorted(counts.items(), key=lambda x: x[1], reverse=True)
text, count = sortcount[0]

print(text, count)
