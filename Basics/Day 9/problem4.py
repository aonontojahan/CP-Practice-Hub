nested = [[1, 2], [3, 4], [5, 6]]

flat = [item for sublist in nested for item in sublist]
print(flat)
