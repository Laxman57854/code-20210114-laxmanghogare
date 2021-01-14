data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

# calculate BMI 
def BMI(height, weight): 
    bmi = weight/(height**2) 
    return bmi 

total = []
# calling the BMI function
try: 
    for dict_ in data:
        bmi = BMI(dict_['HeightCm']/100, dict_['WeightKg']) 
        print("The BMI is", format(bmi), "so ", end='') 
        
        # Conditions to find out BMI category and Health Risk
        if (bmi < 18.4):
            print('Underweight and Health Risk is Malnutrition risk')
        
        elif ( bmi >= 18.4 and bmi < 24.9): 
            print("Normal weight Health Risk is Low risk") 
        
        elif ( bmi >= 25 and bmi < 29.9): 
            print("overweight Health Risk is Enhanced risk")

        elif ( bmi >= 30 and bmi < 34.9):
            total.append(bmi) 
            print("Moderately obese Health Risk is Medium risk")

        elif ( bmi >= 35 and bmi < 39.9): 
            print('Severely obese Health Risk is High risk')

        elif ( bmi >=40): 
            print("Very severely obese Health Risk is Very high risk")
    print('total number overweighted persons', len(total))
except:
    pass