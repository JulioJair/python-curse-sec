class Matrix:

    def __init__(self, matrix=None):
        if matrix is None:
            matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        self.matrix = matrix
        self.n = len(matrix[0])
        self.num_items = self.n * self.n

    def show(self):
        print(f'Given Matrix: {self.matrix}')

    def get_spiral(self):
        spiral = []
        start = 0
        end = self.n - 1
        seen_items = 0
        while (seen_items < self.num_items):
            for i in range(start, end + 1, 1):
                spiral.append(self.matrix[start][i])
                seen_items += 1

            for i in range(start + 1, end + 1, 1):
                spiral.append(self.matrix[i][end])
                seen_items += 1

            for i in range(end - 1, start - 1, -1):
                spiral.append(self.matrix[end][i])
                seen_items += 1

            for i in range(end - 1, start, -1):
                spiral.append(self.matrix[i][start])
                seen_items += 1

            start += 1
            end -= 1
        return spiral


# arreglo = [[1, 3, 3, 4],
#            [5, 6, 7, 8, ],
#            [9, 10, 11, 12],
#            [13, 14, 15, 16]]

m = Matrix()
m.show()
print(m.get_spiral())

