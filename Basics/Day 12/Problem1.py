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

    if arr[mid] == x:
        found_index = mid
        break

    else:
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

print("Result Index:", found_index)
print("Result Value:", arr[found_index] if found_index != -1 else "Not Found")
print("========================")
print("Finding the sum of these subarrays...")