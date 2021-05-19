from .Transpose import transpose


def matrix_formatting(matrix):
    transposed_matrix = transpose(matrix)
    iteration_number = 0

    for point in transposed_matrix[-1]:
        length = len(transposed_matrix[-1])
        if iteration_number != 0 and iteration_number != length - 1:
            transposed_matrix[-1][iteration_number] = ''
        iteration_number += 1

    return transposed_matrix
