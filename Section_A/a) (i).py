#Percentage grade calculation

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    elif 50 <= percentage < 60:
        return "E"
    else:
        return "Fail"

def main():
    while True:
        try:
            percentage = float(input("Enter the percentage: "))
            if 0 <= percentage <= 100:
                grade = calculate_grade(percentage)
                print(f"Grade is {grade}")
                break
            else:
                print("Percentage should be between 0 and 100.")
        except ValueError:
            print("Enter a valid percentage.")

if __name__ == "__main__":
    main()
