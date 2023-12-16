class MatrixOperations:
    @staticmethod
    def add(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = Matrix(matrix1.rows, matrix1.cols)
        for i in range(matrix1.rows):
            for j in range(matrix1.cols):
                result.data[i][j] = matrix1.data[i][j] + matrix2.data[i][j]

        return result

    @staticmethod
    def multiply(matrix1, matrix2):
        if matrix1.cols != matrix2.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")

        result = Matrix(matrix1.rows, matrix2.cols)
        for i in range(matrix1.rows):
            for j in range(matrix2.cols):
                for k in range(matrix1.cols):
                    result.data[i][j] += matrix1.data[i][k] * matrix2.data[k][j]

        return result


# Przyk³ad u¿ycia:
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# U¿ycie klasy MatrixOperations do operacji na macierzach
sum_matrix = MatrixOperations.add(matrix1, matrix2)
print("\nSum of matrices:")
print(sum_matrix)

product_matrix = MatrixOperations.multiply(matrix1, matrix2.transpose())
print("\nProduct of matrices (transposing matrix2):")
print(product_matrix)

# Transpozycja macierzy
transposed_matrix1 = matrix1.transpose()
print("\nTransposed matrix 1:")
print(transposed_matrix1)