def age_calculator():
    try:
        age = int(input("Please tell me your age: "))

        print(f"You are currently {age} years old.")
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    age_calculator()   