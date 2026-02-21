print("practicing CP Day 14")
print("Practicing BACKTRACKING Related Problems")

def generate_subsets(index, current, n):

    if index > n:
        print(current)
        return

    # Choice 1: Include index
    current.append(index)
    generate_subsets(index + 1, current, n)

    # Backtrack
    current.pop()

    # Choice 2: Exclude index
    generate_subsets(index + 1, current, n)


n = int(input())

generate_subsets(1, [], n)