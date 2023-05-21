#removing duplicates
def remove_duplicates(lst):
    return list(set(lst))


numbers = [1, 2, 3, 3, 4, 5, 5, 6]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)


#removing the 0th, 4th and 5th elements
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices_to_remove = [0, 4, 5]

result = [sample_list[i] for i in range(len(sample_list)) if i not in indices_to_remove]
print(result)


#checking primenumbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_numbers(numbers):
    for num in numbers:
        if not is_prime(num):
            return False
    return True


data1 = [0, 3, 4, 7, 9]
print(check_prime_numbers(data1))  

data2 = [3, 5, 7, 13]
print(check_prime_numbers(data2))  

data3 = [1, 5, 3]
print(check_prime_numbers(data3))  



