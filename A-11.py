height = float(input("Height(m)? > "))
weight = float(input("Weight(kg)? > "))

user_bmi = round(weight / height ** 2, 2)

print(f"Your BMI is {user_bmi}")
