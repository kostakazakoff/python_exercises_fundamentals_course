source_start = ['a', 'b']
source_end = ['c', 'd']
str_to_divide = '1234567'
divided_str = ''
step = 2
dev_left = 1
while len(str_to_divide) > 0:
    divided_str += str_to_divide[:step] + ' '
    str_to_divide = str_to_divide[step:]
divided_str = (divided_str.strip())
divided_list = divided_str.split()
if dev_left > 0:
    divided_list = divided_list[:-2] + [''.join(divided_list[-2:])]
result = source_start + divided_list + source_end

print(result)