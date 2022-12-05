import string
from functools import reduce

# read the inputs
with open('inputs/03.txt', 'r') as f:
    input = f.read()

# input clean up
input_list = input.split('\n')


### PART 1
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


### PART 2
end = len(input_list)
step = 3
common_elements = []

for i in range(0, len(input_list), step):
    # split input into 3-member groups
    group_of_3 = input_list[i:i+step]

    # identify a common element
    common_element = reduce(lambda x, y: set(x).intersection(set(y)), group_of_3)
    common_elements.append(list(common_element))

flat_common_elements = [item for sublist in common_elements for item in sublist]

# find priorities and their sum
total_sum = 0
for element in flat_common_elements:
    total_sum += priorities[element]

## answer
total_sum