name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = {}

for line in handle:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 5:
            hour = words[5][:2]
            counts[hour] = counts.get(hour, 0) + 1

sortcounts = sorted(counts.items())
for hour, count in sortcounts:
    print(hour, count)
