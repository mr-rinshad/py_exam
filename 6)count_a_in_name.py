names = input("Enter first names: ").split()

count_a = 0
for name in names:
    count_a += name.lower().count('a')

print("Total 'a' count:", count_a)
