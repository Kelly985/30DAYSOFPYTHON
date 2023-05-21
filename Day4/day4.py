def calculate_sum(numbers):
    return sum(numbers)


def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest


def print_intro(name, age, occupation):
    print(f"My name is {name}, I am {age} years old and I work as a {occupation}.")


numbers = [9, 2, 3, 7, 5]
print(calculate_sum(numbers))

numbers = [5, 2, 9, 9, 7]
print(find_second_largest(numbers))


print_intro("kelly", 22, "software Engineer")

