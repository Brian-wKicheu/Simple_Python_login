age = int(input("enter your age\n"))
if age >= 70:
    print("You qualify for NHIf only")
else:
    if age <= 18:
        print("You qualify for child support only and ")
    elif age > 18:
        print("You don't qualify for child support and ")
    print("You don't qualify for NHIf")
