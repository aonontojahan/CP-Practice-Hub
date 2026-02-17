n = int(input())

arr = list(map(int, input().split()))

k = int(input())

left = 0
right = 0

current_sum = 0
max_length = 0

while right < n:

    # Expand window
    current_sum = current_sum + arr[right]

    print("Added:", arr[right])
    print("Current Sum:", current_sum)

    # Shrink window if sum exceeds k
    while current_sum > k and left <= right:

        print("Removing:", arr[left])

        current_sum = current_sum - arr[left]
        left = left + 1

        print("New Sum After Removal:", current_sum)

    # Update maximum length
    window_length = right - left + 1

    if window_length > max_length:
        max_length = window_length

    print("Window:", left, "to", right)
    print("Window Length:", window_length)
    print("----------------------------")

    right = right + 1

print("Maximum Length of Subarray with Sum <=", k, "=", max_length)
print("==========================")