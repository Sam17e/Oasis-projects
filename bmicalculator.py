height=float(input("Enter Your Height(m) :"))
weight=float(input("Enter Your Weight(kg) :"))
bmi=weight/(height**2)
print("Your Body Mass Indes is",bmi)
if bmi <=18.5:
    print("Your are under weight")
elif bmi <=24.9:
    print("Awsome! You are Normal")
elif bmi <=29.9:
    print("You are over weight")
else:
    print("You are obese")
