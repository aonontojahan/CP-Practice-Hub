print("Practicing CP Day 14")
def generate_permutations(arr, used, current):

    if len(current) == len(arr):
        print(current)
        return

    i = 0
    while i < len(arr):

        if used[i] == False:

            used[i] = True
            current.append(arr[i])

            generate_permutations(arr, used, current)

            # Backtrack
            current.pop()
            used[i] = False

        i = i + 1


arr = list(map(int, input().split()))

used = [False] * len(arr)

generate_permutations(arr, used, [])