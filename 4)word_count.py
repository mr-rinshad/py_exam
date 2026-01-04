text=input("enter text : ").split()
count ={}

for w in text:
    if w in count:
        count[w]+=1
    else:
        count[w]=1
print(count)