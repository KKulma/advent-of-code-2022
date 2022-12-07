## Today's assignment defeated me! Here's the solution I liked that I got from reddit https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz9p2ki/?utm_source=share&utm_medium=web2x&context=3
# essentailly, I tried to create a JSON-like dictionary with path dirs and file sizes, didn't occur to me to that I can use actual paths and lists
with open('inputs/07.txt', 'r') as f:
    input = f.read()

input_list = input.split('\n')

# input_list = [
#     '$ cd /',
#     '$ ls',
#     'dir a',
#     '14848514 b.txt',
#     '8504156 c.dat',
#     'dir d',
#     '$ cd a',
#     '$ ls',
#     'dir e',
#     '29116 f',
#     '2557 g',
#     '62596 h.lst',
#     '$ cd e',
#     '$ ls',
#     '584 i',
#     '$ cd ..',
#     '$ cd ..',
#     '$ cd d',
#     '$ ls',
#     '4060174 j',
#     '8033020 d.log',
#     '5626152 d.ext',
#     '7214296 k'
# ]

parent_dirs = []
dir_sizes = {}

for line in input_list:
    line = line.split(' ')
    if line[0] == '$':
        if line[1] == 'cd' and line[2] != '..':
            parent_dirs.append(line[2])
            dir_sizes['/'.join(parent_dirs)] = 0
            print(parent_dirs)
            print(dir_sizes)
        elif line[1] == 'cd' and line[2] == '..':
            parent_dirs.pop()
    elif line[0].isnumeric():
        temp_parent_dirs = parent_dirs.copy()
        while len(temp_parent_dirs) > 0:
            dir_sizes['/'.join(temp_parent_dirs)] += int(line[0])
            temp_parent_dirs.pop()

print(f"Size of all directories: {dir_sizes}")
small_dirs = { key:value for (key,value) in dir_sizes.items() if value <= 100000 }
print(f"Directories that are <= 100000: {small_dirs}")
print(f"Sum of all small diretories: {sum(small_dirs.values())}")
