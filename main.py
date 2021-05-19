from Utils.ReadWriteData import read_data
from Utils.ReadWriteData import write_data
from Utils.MatrixFormatting import matrix_formatting

width, height, matrix, points = read_data('ijones.in')


def find_paths(matrix, width):
    letters_dictionary = dict((key, [0] * width) for key in points)
    matching_nghbr = dict((key, [0] * width) for key in points)
    column_index = 0

    for column in matrix:
        item_index = 0
        for item in column:
            if item:
                letters_dictionary[item][column_index] += 1
                if column_index > 0 and item != matrix[column_index - 1][item_index]:
                    matching_nghbr[item][column_index] += 1
                    letters_dictionary[item][column_index] *= \
                        letters_dictionary[matrix[column_index - 1][item_index]][column_index - 1]
            item_index += 1

        for item in set(column):
            if item and column_index > 0:
                if sum((letters_dictionary[item])[:column_index]) != 0:
                    letters_dictionary[item][column_index] *= sum((letters_dictionary[item])[:column_index])
                    letters_dictionary[item][column_index] += matching_nghbr[item][column_index]
        column_index += 1

    return letters_dictionary


if __name__ == "__main__":
    matrix = matrix_formatting(matrix)
    result_dict = find_paths(matrix, width)
    write_data('ijones.out', result_dict)
