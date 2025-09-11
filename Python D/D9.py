import math
print("Matrix Concepts:-")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col],end=" ")
    print()

even_list = [x for row in matrix for x in row if  x%2 ==0]
squared_list = [x for row in matrix for x in row if (math.sqrt(x))%1 == 0 ]
print(even_list)
print(squared_list)

print("Transpose of the matrix")
# trans = [[],[],[]]
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         trans[row][col].append( matrix[col][row])
trans = list(map(list,zip(*matrix))) 
flatten = [x for row in matrix for x in row]
print(*matrix)
print(*trans)
print(*flatten)