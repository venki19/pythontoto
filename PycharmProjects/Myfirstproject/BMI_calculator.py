
def calculate_bmi(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi


weight = float(input("please enter weight in kgs"))
height = float(input("please enter height in meters"))
bmi = calculate_bmi(weight, height)
print(bmi)
