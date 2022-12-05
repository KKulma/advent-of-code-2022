# read the inputs
with open('inputs/04.txt', 'r') as f:
    input = f.read()

# input clean up
input_list = input.split('\n')


# ### PART 1
input_list = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]

overlaps = []
ranges_list = []
for element in input_list:
    range_input = [[int(i[0]), int(i[2])+1] for i in element.split(',')]
    ranges = [list(range(i[0], i[1])) for i in range_input]
    common_elements = set(ranges[0]).intersection(set(ranges[1]))
    overlaps.append(list(common_elements))
    ranges_list.append(ranges)

full_overlaps = 0
for index, data in enumerate(overlaps):
    if len(data)>0:
        range_data = ranges_list[index]
        for range in range_data:
            if range == data:
                full_overlaps += 1
# answer
full_overlaps

### PART 2