import math

start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))
result=[]

for num in range(start,end+1):
    if 1000<=num<=9999 and all(int(d)%2==0 for d in str(num)) and int(math.sqrt(num))**2==num:
        result.append(num)

print(result)
