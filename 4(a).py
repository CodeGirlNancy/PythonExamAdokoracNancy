# University Bonuses

def calculate_bonus_salary(salary, years_of_service):
    if years_of_service > 4:
        bonus_percentage = 8
    elif years_of_service == 3:
        bonus_percentage = 5
    else:
        bonus_percentage = 0
    
    bonus_amount = (bonus_percentage / 100) * salary
    net_salary = salary + bonus_amount
    
    return bonus_amount, net_salary

def main():
    while True:
        try:
            salary = float(input("Enter your salary: "))
            years_of_service = int(input("Enter your years of service: "))

            bonus_amount, net_salary = calculate_bonus_salary(salary, years_of_service)

            print(f"Net bonus amount: {bonus_amount}")
            print(f"Net salary amount: {net_salary}")

            choice = input("Woul you wish to continue? (yes/no): ")
            if choice.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
