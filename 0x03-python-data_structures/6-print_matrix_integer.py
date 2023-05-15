def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == ln(row) - 1:
                print("{}".format(row[i]), end="")
	    else:
                print("{} ".format(row[i]), end="")
         print()
