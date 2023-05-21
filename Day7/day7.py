#find all the unique combinations of 3 numbers from a given list of numbers
from itertools import combinations

def find_combinations(numbers, target):
    return [comb for comb in combinations(numbers, 3) if sum(comb) == target]

# Example usage:
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 15
combinations = find_combinations(number_list, target_sum)
for combination in combinations:
    print(combination)
