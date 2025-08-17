import os

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def estimate_bodyfat(bmi, age, gender):
    if gender == "m":
        return 1.20 * bmi + 0.23 * age - 16.2
    elif gender == "f":
        return 1.20 * bmi + 0.23 * age - 5.4
    else:
        return None


def BMIcategorize(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.99:
        return "Healthy weight"
    elif 25 <= bmi <= 29.99:
        return "Overweight"
    else:
        return "Obese"
    

def tips(category, age, gender):
    print("Health tips for you!\n")
    if category == "Underweight":
        print("Try to eat more nutritious food like rice, beans and egg if possible!")
        print("Also workout and drink a lot of water!\n")
    elif category == "Healthy weight":
        print("Awesome! You're very healthy right now, try to keep this ongoing!")
        print("Don't forget to exercise regularly and eat balanced meal!\n")
    elif category == "Overweight":
        print("This doesn't mean you're fat! It can also mean you have muscles!")
        print("Consider walking 20 to 30 minutes if you want to lose weight and try to cut sugar if possible!\n")
    else:
        print("Start with small physical activities like stretching or just go for a walk!")
        print("Focus on diet meals - less oil, sugar and calories!\n")


    print("\nAdditional tip based on your age:")
    if age < 18:
        print("As a teenager, focus on healthy eating and stay active!")
    elif 18 <= age <= 50:
        print("Keep a balanced routine - work, meals, and exercise!")
    else:
        print("At your age, staying active and eating lighter becomes more important!")

    if gender == "m":
        print("\nFor men: Try including strength training in your routine.")
    elif gender == "f":
        print("\nFor women: Focus on foods that are rich in calcium try including light cardio in your routine.")
    else:
        print("\nTip: Customize your fitness and food to what feels right for you.")
    

def intro():
    question1 = input("Do you know what BMI is? (1 = Yes, 2 = No): ")
    if question1 == "1":
        print("Excellent! Let's move on to the next part!\n")
    elif question1 == "2":
        print("BMI is a number that helps you understand if you're at a healthy weight or not!")
        print("Let's move on to the next part!\n")
    else:
        print("Oops invalid input! But let's move on anyway.\n")


def range():
    print("\nBMI Ranges:\n")
    print("Under 18.5 ➡ Underweight")
    print("18.5 - 24.99 ➡ Healthy weight")
    print("25 - 29.99 ➡ Overweight")
    print("30 and above ➡ Obese\n")


def metric():
    while True:
        try:
            weight = float(input("\nPlease enter your weight in kilograms (kg): "))
            height = float(input("Please enter your height in meters (m): "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive values!")
                continue

            return weight, height
        
        except ValueError:
            print("Please enter valid numbers!")


def imperial():
    while True:
        try:
            weight_lbs = float(input("\nPlease enter your weight in pounds (lbs): "))
            height_feet = float(input("Please enter your height in feet (We will ask your inches later so you don't have to write it here!): "))
            height_inches = float(input("Please enter your height in inches: "))
            if weight_lbs <= 0 or height_feet <= 0 or height_inches <= 0:
                print("All values must be positive!")
                continue

            weight = weight_lbs * 0.453592
            total_inches = (height_feet * 12) + height_inches
            height = total_inches * 0.0254

            return weight, height
    
        except ValueError:
            print("Please enter valid numbers!")


def education_module():
    print("\nHealth Education Module")

    print("\nNutrition Tips on a Budget: ")
    print("- Eat local and seasonal fruits and vegetables.")
    print("- Include affordable protein: eggs, beans, lentils.")
    print("- Avoid sugar drinks and fried snacks.")

    print("\nExercise Without a Gym: ")
    print("- Walking, stretching, climbing stairs.")
    print("- Dancing, house chores, skipping rope.")

    print("\nMental Health Tips: ")
    print("- Get enough sleep and limit screen time.")
    print("- Talk to someone if you're feeling overwhelmed.")

    input("\nPress Enter to return to the main menu...")


def start():
    while True:
        while True:
            try:
                age = int(input("\nPlease enter your age: "))
                break

            except ValueError:
                print("Please enter a valid number for your age!")

        gender_input = input("Enter your gender (M/F/Other): ").strip().lower()
        if gender_input.startswith("m"):
            gender = 'm'
        elif gender_input.startswith("f"):
            gender = 'f'
        else:
            gender = 'other'
            print("Gender input not recognized. Proceding with general recommendations.")

        print("\nChoose your prefer unit system: ")
        print("1. Metric (kg, meters)")
        print("2. Imperial (lbs, feet + inches)")

        unit_choice = input("Enter 1 or 2: ")
        if unit_choice == "1":
            weight, height = metric()
        elif unit_choice == "2":
            weight, height = imperial()
        else:
            print("Oops invalid input! Returning to main menu...\n")
            return
    
        bmi = calculate_bmi(weight, height)
        category = BMIcategorize(bmi)
        bodyfat = estimate_bodyfat(bmi, age, gender)

        print("\nYour BMI is: ", round(bmi, 3))
        print("Based on your BMI, you are classified as:", category + "\n")

        if bodyfat is not None:
            print(f"Estimated Body Fat %: {round(bodyfat, 2)}%")

        print("\nActivity Level: ")
        print("1. Sedentary (little to no exercise)")
        print("2. Lightly active (1-3 days/week)")
        print("3. Active (4-6 days/week)")
        activity = input("Choose 1, 2 or 3: ")
        factor = {"1": 1.2, "2": 1.55, "3": 1.9}.get(activity, 1.2)

        if gender == "m":
            bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
        elif gender == "f":
            bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161
        else:
            bmr = 10 * weight + 6.25 * height * 100 - 5 * age

        tdee = bmr * factor
        print(f"- Estimated TDEE: {round(tdee)} kcal/day\n")

        print("Your Goal: ")
        print("1. Lose weight")
        print("2. Maintain weight")
        print("3. Gain weight/muscle")
        goal = input("Chooses 1, 2 or 3: ")

        print("\nRecommendation: ")
        if goal == "1":
            print(f"- Eat about {round(tdee - 300)} to {round(tdee - 500)} kcal/day to lose weight.\n")
        elif goal == "2":
            print(f"- Maintain around {round(tdee)} kcal/day.\n")
        elif goal == "3":
            print(f"- Eat about {round(tdee + 250)} to {round(tdee + 500)} kcal/day to gain weight/muscle.\n")
        else:
            print("- Goal not recognized. Use TDEE for reference.\n")

        tips(category, age, gender)

        save = input("\nSave your results to a file? (y/n): ").lower()
        if save == "y":
            with open("bmi_report.txt", "a") as file:
                file.write(f"Age: {age}, Gender: {gender}, BMI: {round(bmi, 2)}, Category: {category}, Body Fat: {round(bodyfat, 2) if bodyfat else 'N/A'}%, TDEE: {round(tdee)} kcal, Goal: {goal}\n")
            print (os.path.abspath("bmi_report.txt"))
            print("Results saved to 'bmi_report.txt'.")


        print("\nDo you want to calculate another BMI?")

        restart = input("Please enter y for yes and n for no: \n").lower()
        if restart != "y":
            break


def menu():
    while True:
        print("\nWelcome to the BMI Calculator!")
        print("1. Learn about BMI")
        print("2. What is the range of BMI?")
        print("3. Calculate your BMI")
        print("4. Learn about Health & Nutrition")
        print("5. Exit")

        menu_choice = input("Enter your choice (1, 2, 3, 4 or 5): ")
        if menu_choice == "1":
            intro()
            range()
            start()
        elif menu_choice == "2":
            range()
            start()
        elif menu_choice == "3":
            start()
        elif menu_choice == "4":
            education_module()
        elif menu_choice == "5":
            print("Goodbye! Stay healthy and see you next time 💪")
            break
        else:
            print("Please enter the right number")
            

menu()