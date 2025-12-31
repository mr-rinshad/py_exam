n = int(input("Enter number of terms: "))

t0 = 0
t1 = 1

for i in range(n):
    print(t0, end=" ")
    t2 = t0 + t1
    t0 = t1
    t1 = t2
