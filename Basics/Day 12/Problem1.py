n = int(input())

arr = list(map(int, input().split()))

x = int(input())

left = 0
right = n - 1
found_index = -1

while left <= right:

    mid = (left + right) // 2

    print("Left:", left)
    print("Right:", right)
    print("Mid:", mid)
    print("Mid Value:", arr[mid])
    print("------------------------")

