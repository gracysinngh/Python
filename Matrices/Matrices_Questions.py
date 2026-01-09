# 1.You are given two matrices 𝐴 and 𝐵. Write a program that performs the following operations on these matrices and prints the result for each operation:

# Addition of matrices 𝐴 and 𝐵
# Subtraction of matrix 𝐵 from 𝐴
# Multiplication of matrices 𝐴 and 𝐵
# Transpose of matrix 𝐴
# Diagonal sum of matrix 𝐴 and matrix 𝐵


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

def add_matrices(A, B):
    x = len(A)
    y = len(A[0])
    mat = []
    for i in range(x):
        row =[]
        for j in range(y):
            ele = A[i][j]+B[i][j]
            row.append(ele)
        mat.append(row)    
    # write your code here
    return mat

def subtract_matrices(A, B):
    # write your code here
    x = len(A)
    y = len(A[0])
    mat = []
    for i in range(x):
        row =[]
        for j in range(y):
            row.append(A[i][j]- B[i][j])
        mat.append(row)    
    return mat

def multiply_matrices(A, B):
    x = len(A)
    y = len(B[0])
    z = len(B)  # or len(A[0])

    # Initialize result matrix with zeros
    mat = [[0 for _ in range(y)] for _ in range(x)]

    # Perform multiplication
    for i in range(x):
        for j in range(y):
            for k in range(z):
                mat[i][j] += A[i][k] * B[k][j]

    return mat

def transpose_matrix(A):
    x = len(A)
    y = len(A[0])
    mat = []
    for j in range(y):
        row = []
        for i in range(x):
            row.append(A[i][j])
        mat.append(row)
    return mat

def diagonal_sum(A):
    # write your code here
    n = len(A)
    summ = 0
    for i in range(n):
        summ+=A[i][i]
    return summ

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    A = []
    B = []
    for i in range(n):
        A.append([int(data[index + j]) for j in range(m)])
        index += m
    for i in range(n):
        B.append([int(data[index + j]) for j in range(m)])
        index += m
    
    print("Addition:")
    add_result = add_matrices(A, B)
    print_matrix(add_result)
    
    print("Subtraction:")
    sub_result = subtract_matrices(A, B)
    print_matrix(sub_result)
    
    print("Multiplication:")
    mul_result = multiply_matrices(A, B)
    print_matrix(mul_result)
    
    print("Transpose of A:")
    trans_result = transpose_matrix(A)
    print_matrix(trans_result)
    
    print("Diagonal Sum of A:", diagonal_sum(A))
    print("Diagonal Sum of B:", diagonal_sum(B))




# 2.You are given two matrices A and B. Your task is to multiply them, but only if they are dimensionally compatible. If they are not compatible (i.e., the number of columns in A is not equal to the number of rows in B), print "Incompatible dimensions".

# Note that maximum size of matrix can be 3


# Use print() to print to the console
def read_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError("Row does not match expected column count")
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    if not B or not B[0]:
        print("Incompatible dimensions")
        return
    n = len(A)
    m = len(A[0])
    p = len(B)
    q = len(B[0])

    if m != p:
        print("Incompatible dimensions")
        return

    # Initialize result matrix
    result = [[0 for _ in range(q)] for _ in range(n)]

    # Perform multiplication
    for i in range(n):
        for j in range(q):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]

    # Print result
    for row in result:
        print(" ".join(map(str, row)))

# Read dimensions and matrix A
n, m = map(int, input().split())
A = read_matrix(n, m)

# Read dimensions and matrix B
p, q = map(int, input().split())
B = read_matrix(p, q)

# Multiply if compatible
multiply_matrices(A, B)





# 3. You are given a square matrix of size n x n. Your task is to rotate the matrix by 90 degrees clockwise and print the resulting matrix.


def rotate_matrix(matrix, n):
    # Write code here
    rotated = []

    for i in range(n):
        new_row = []

        for j in range(n - 1, -1, -1):
            new_row.append(matrix[j][i])

        rotated.append(new_row)

    return rotated

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    rotated_matrix = rotate_matrix(matrix, n)

    for row in rotated_matrix:
        print(*row)  # Print elements separated by spaces


