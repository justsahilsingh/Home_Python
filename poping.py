num1=[2,3,3,2]
val=2
for i in num1:
    if i!=val:
        num1.append(i)
        i+=1
        print(num1)
