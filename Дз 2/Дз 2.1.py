list = (1, 'dva', 3.3, 4+4j, True, [1, 2], (1, 2), {1: 'one', 2: 'two'}, {9, 10}, frozenset(), range(12), b'thirdteen', bytearray(b'fourteen'), TypeError)
for i, val in enumerate(list, 1):
    print(f'{i}) {val} - {type(val)}')
