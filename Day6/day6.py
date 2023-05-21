#combine two dictionary by adding values for common keys.
from collections import Counter

def combine_dictionaries(d1, d2):
    return Counter(d1) + Counter(d2)


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = combine_dictionaries(d1, d2)
print(combined_dict)


#create a dictionary from a string
def create_letter_count_dict(string):
    letter_count = {}
    for char in string:
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count


string = 'w3resource'
result = create_letter_count_dict(string)
print(result)
