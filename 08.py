import numpy as np

with open('inputs/08.txt', 'r') as f:
    input = f.read()

input_list = input.split('\n')

# input_list = [
#     '30373',
#     '25512',
#     '65332',
#     '33549',
#     '35390'
# ]


matrix = []
for i in input_list:
    row_list = []
    for j in range(len(i)):
        row_list.append(int(i[j]))
    matrix.append(row_list)

final_matrix = np.array(matrix)
range_list = list(range(len(final_matrix)))
index_lookup = dict(zip(range_list, range_list[::-1]))


###### PART 1
visible_trees = []
#### look right #####
for row_index, row in enumerate(final_matrix):
    trees_so_far = []
    for tree_index, tree in enumerate(row):
        if tree_index == 0:
            trees_so_far.append(tree)
            visible_trees.append((row_index, tree_index))
        else:
            if all([tree_so_far < tree for tree_so_far in trees_so_far]):
                visible_trees.append((row_index, tree_index))
                trees_so_far.append(tree)

####### look down ########
final_matrix_cols = np.vstack([final_matrix[..., col] for col in range_list])
for row_index, row in enumerate(final_matrix_cols):
    trees_so_far = []
    for tree_index, tree in enumerate(row):
        if tree_index == 0:
            trees_so_far.append(tree)
            visible_trees.append((tree_index, row_index))
        else:
            if all([tree_so_far < tree for tree_so_far in trees_so_far]):
                visible_trees.append((tree_index, row_index))
                trees_so_far.append(tree)

##### look up ####
matrix_inv_cols = np.vstack([final_matrix[..., col][::-1] for col in range_list])
for row_index, row in enumerate(matrix_inv_cols):
    trees_so_far = []
    for tree_index, tree in enumerate(row):
        if tree_index == 0:
            trees_so_far.append(tree)
            visible_trees.append((index_lookup[tree_index], row_index))
        else:
            if all([tree_so_far < tree for tree_so_far in trees_so_far]):
                visible_trees.append((index_lookup[tree_index], row_index))
                trees_so_far.append(tree)

##### look left ####
matrix_inv_rows = np.vstack([row[::-1] for row in final_matrix])
for row_index, row in enumerate(matrix_inv_rows):
    trees_so_far = []
    for tree_index, tree in enumerate(row):
        if tree_index == 0:
            trees_so_far.append(tree)
            visible_trees.append((row_index, index_lookup[tree_index]))
        else:
            if all([tree_so_far < tree for tree_so_far in trees_so_far]):
                visible_trees.append((row_index, index_lookup[tree_index]))
                trees_so_far.append(tree)

## answer
len(set(visible_trees))
