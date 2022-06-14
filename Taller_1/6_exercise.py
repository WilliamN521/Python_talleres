"""
6 Exercise
----------
Fix the result of the sum of each list

matrix = [
            [2, 4, 3, 6],
            [8, 3, 4, 5],
            [7, 1, 3, 10],
            [9, 2, 1, 4]
        ]
"""
matrix = [
            [2, 4, 3, 6],
            [8, 3, 4, 5],
            [7, 1, 3, 10],
            [9, 2, 1, 4]
        ]

print(f"\nOriginal matrix\n{matrix}")

# solution with slicing 1 and 2 row
matrix[0][-1] = sum(matrix[0][:3])
matrix[1][-1] = sum(matrix[1][:3])

# solution with append 3 row
matrix[2] = matrix[2][:3]
matrix[2].append(sum(matrix[2]))
# solution with append 4 row
matrix[3] = matrix[3][:3]
matrix[3].append(sum(matrix[3]))

# show the results
print(f"\nFinal matrix\n{matrix}")