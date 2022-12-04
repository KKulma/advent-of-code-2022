import string
# read the inputs
with open('inputs/03.txt', 'r') as f:
    input = f.read()

# input clean up
input_list = input.split('\n')

# input_list = [
#     'vJrwpWtwJgWrhcsFMMfFFhFp',
#     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#     'PmmdzqPrVvPwwTWBwg',
#     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#     'ttgJtRGJQctTZtZT',
#     'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]

common_elements = []
for element in input_list:
    half_index = int(len(element)/2)
    bag1 = element[:half_index]
    bag2 = element[half_index:]
    common_element = list(set(bag1).intersection(bag2))
    common_elements.append(common_element)

flat_common_elements = [item for sublist in common_elements for item in sublist]


priorities = dict(zip(string.ascii_lowercase+string.ascii_uppercase, list(range(1, 53))))

total_sum = 0
for element in flat_common_elements:
    total_sum += priorities[element]

## answer
total_sum
