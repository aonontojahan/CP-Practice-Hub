lst = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for item in lst:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)
print("Program is over")
