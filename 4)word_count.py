text = input("Enter text: ")

words = text.split()
count = {}

for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

print(count)

