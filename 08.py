#with open('inputs/08.txt', 'r') as f:
#     input = f.read()
#
# input_list = input.split('\n')

input_list = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390'
]
final_matrix = []
for i in input_list:
    row_list = []
    for j in range(len(i)):
        row_list.append(int(i[j]))
    final_matrix.append(row_list)


visible_trees = []
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




