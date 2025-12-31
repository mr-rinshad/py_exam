list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

# (a) Check same length
if len(list1) == len(list2):
    print("Lists are of same length")
else:
    print("Lists are of different length")

# (b) Check same sum
if sum(list1) == sum(list2):
    print("Lists have same sum")
else:
    print("Lists have different sum")

# (c) Check common values using set
common = set(list1) & set(list2)

if common:
    print("Common values exist:", common)
else:
    print("No common values")
