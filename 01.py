# read the inputs
with open('inputs/01.txt', 'r') as f:
    input = f.read()

# input clean up
input_list = input.split('\n')


### FIRST QUESTION ###
# separate inputs into sublists
mini_list = []
final_list = []
for element in input_list:
    if element != '':
        mini_list.append(int(element))
    else:
        final_list.append(mini_list)
        mini_list = []
print(final_list)

# sort in descending order
sums = [sum(mini_list) for mini_list in final_list]
sums.sort(reverse=True)

# answer
print(sums[0])

### SECOND QUESTION ###

print(sum(sums[0:3]))