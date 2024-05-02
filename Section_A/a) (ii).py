#Temperature Conversion

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius equals to {fahrenheit} Fahrenheit.")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit equals to {celsius} Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
