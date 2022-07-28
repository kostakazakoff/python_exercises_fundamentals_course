import re


def barcode_validation():
    if not match:
        print('Invalid barcode')
        return
    barcode = match.group('barcode')
    p_group = ''.join([x for x in barcode if x.isdigit()])
    if not p_group:
        p_group = '00'
    print(f'Product group: {p_group}')


str_count = int(input())

for _ in range(str_count):
    barcode_pattern = r'(@{1}#+)(?P<barcode>\b[A-Z]{1}[A-Za-z\d]{4,}[A-Z]{1}\b)(@{1}#+)'
    match = re.search(barcode_pattern, input())
    barcode_validation()
