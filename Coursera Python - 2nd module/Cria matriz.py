nr_lines = int(input("Number of lines: "))
nr_columns = int(input("Number of columns: "))

matrix = []
for i in range(nr_lines):
    lines = []
    for j in range(nr_columns):
        lines.append(0)  # Appends only 0 to all the elements of the matrix.
    matrix.append(lines)

for i in range(nr_lines):
    print(matrix[i], end = '\n')
