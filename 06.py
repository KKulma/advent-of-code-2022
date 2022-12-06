## PART 1

# define a function
def find_marker(input, n):
    start_position = 0
    dist_chars = 0

    while dist_chars != n:
        test_char = input[start_position:start_position + n]
        dist_chars = len(set(test_char))
        start_position += 1

        if start_position >= (len(input)-n):
            break
    else:
        print(test_char)
        print(f'start_position: {start_position}')
        print(f'answer: {start_position + (n - 1)}')

# read the inputs
with open('inputs/06.txt', 'r') as f:
    input = f.read()

## PART 1
find_marker(input, 4)

### PART 2
find_marker(input, 14)
