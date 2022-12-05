# read the inputs
with open('inputs/04.txt', 'r') as f:
    input = f.read()

# input clean up
input_list = input.split('\n')


# ### PART 1
# input_list = [
#     '2-4,6-8',
#     '2-3,4-5',
#     '5-7,7-9',
#     '2-8,3-7',
#     '6-6,4-6',
#     '2-6,4-8'
# ]

full_overlaps = 0
for element in input_list:
# element = input_list[0]
    range_input_str = [i.split('-') for i in element.split(',')]
    range_input_int = [list(map(int, j)) for j in range_input_str]
    x1, y1 = range_input_int[0]
    x2, y2 = range_input_int[1]
    if (x1 <= x2 and y1 >= y2) or (x2 <= x1 and y2 >= y1):
        full_overlaps+=1




### PART 2