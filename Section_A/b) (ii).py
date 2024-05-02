#Using a loop

def sum_list_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# i.e.given sample,
numbers = [9, 2, 3, 5, 8]
print("Sum of numbers in the list:", sum_list_numbers(numbers))
