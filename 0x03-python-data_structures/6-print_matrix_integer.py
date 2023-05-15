def print_matrix_integer(matrix=None):
    if matrix is None:
        matrix = []
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{}".format(row[i]), end="")
            else:
                print("{} ".format(row[i]), end="")
    print()
