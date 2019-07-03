h = int(input("Enter your height (cm): "))
m = int(input("Enter your weight (kg): "))

h *= 0.01
bmi = m/(h**2) 
print("Your BMI is:",bmi)

if bmi < 16:
    print("You're severely underweight.")
elif bmi < 18.5:
    print("You're underweight.")
elif bmi < 25: 
    print("You're normal.")
elif bmi < 30:
    print("You're overweight.")
else:
    print("You're obese.")