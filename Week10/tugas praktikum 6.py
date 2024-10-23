array1 = [
    [4, 6],
    [1, 7]
]

array2 = [
    [2, 3],
    [5, 6]
]

print ("\nHasil penjumlahan dari array tersebut:")
for x in range(0, len(array1)):
    for y in range(0, len(array1[0])):
        print (array1[x][y] + array2[x][y], end=' '),
    print()

print ("\nHasil pengurangan dari array tersebut:")
for x in range(0, len(array1)):
    for y in range(0, len(array1[0])):
        print (array1[x][y] - array2[x][y], end=' '),
    print()