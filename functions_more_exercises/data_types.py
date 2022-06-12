type = input()
source = input()


def data_types(datatype, string):
    if 'int' in type:
        result = int(source) * 2
    elif 'real' in type:
        result = f'{float(source) * 1.5:.2f}'
    elif 'string' in type:
        result = f'${source}$'
    return result


print(data_types(type, source))