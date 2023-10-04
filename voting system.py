def aligible_voting(age):
    if age>=18:
        print("Eligible for voting")
    else:
        print("not elegible")

age=int(input("Enter age: "))
aligible_voting(age)
