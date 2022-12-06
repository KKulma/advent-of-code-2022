### PART 1
import re

# read the inputs
with open('inputs/05.txt', 'r') as f:
    input = f.readlines()[10:]

commands = [ele.replace('\n', '') for ele in input]

cargos = [
    'WMLF',
    'BZVMF',
    'HVRSLQ',
    'FSVQPMTJ',
    'LSW',
    'FVPMRJW',
    'JQCPNRF',
    'VHPSZWRB',
    'BMJCGHZW'
]
keys = [f'crate_{i}' for i in range(1, 10)]
crate_dict = dict(zip(keys, cargos))

for x in commands:
    # find number of digits through regular expression
    raw_digits = re.findall(r'\d+', x)
    digits = list(map(int, raw_digits))
    qnt = digits[0]
    move_from = f'crate_{digits[1]}'
    move_to = f'crate_{digits[2]}'

    # select and swap order
    select = crate_dict[move_from][-qnt:]
    cargo = select[::-1]
    # final action - drop
    new_from_length = len(crate_dict[move_from])-qnt
    new_from_value = crate_dict[move_from][:new_from_length]
    new_to_value = crate_dict[move_to]+cargo
    crate_dict.update({
        move_from: new_from_value,
        move_to: new_to_value
    })

# answer
''.join([value[-1] for value in crate_dict.values()])


### PART 2
# crate_dict = {
#     'crate_1': 'ZN',
#     'crate_2': 'MCD',
#     'crate_3': 'P'
# }
#
# commands = [
#     'move 1 from 2 to 1',
#     'move 3 from 1 to 3',
#     'move 2 from 2 to 1',
#     'move 1 from 1 to 2'
# ]

for x in commands:
    # find number of digits through regular expression
    raw_digits = re.findall(r'\d+', x)
    digits = list(map(int, raw_digits))
    qnt = digits[0]
    move_from = f'crate_{digits[1]}'
    move_to = f'crate_{digits[2]}'

    # select and swap order
    cargo = crate_dict[move_from][-qnt:]
    # final action - drop
    new_from_length = len(crate_dict[move_from])-qnt
    new_from_value = crate_dict[move_from][:new_from_length]
    new_to_value = crate_dict[move_to]+cargo
    crate_dict.update({
        move_from: new_from_value,
        move_to: new_to_value
    })

# answer
''.join([value[-1] for value in crate_dict.values()])