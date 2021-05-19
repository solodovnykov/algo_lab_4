from .Calculate import calculate_result


def read_data(filename: str):
    matrix = []
    points = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        width, height = tuple(int(x) for x in lines[0].split())
        for line in lines[1:]:
            for char in line:
                if char != '\n':
                    points.append(char)
            matrix_line_format = list(line.replace('\n', ''))
            matrix.append(matrix_line_format)

    return width, height, matrix, set(points)


def write_data(filename: str, data):
    with open(filename, "w") as output_file:
        output_file.write(str(calculate_result(data)))
