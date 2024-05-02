#Calculating the area of a triangle

def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

def main():
    
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle: "))


    area = calculate_triangle_area(base, height)

  
    print("The area of the triangle is:", area)

if __name__ == "__main__":
    main()
