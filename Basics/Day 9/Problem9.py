n = int(input())

arr = list(map(int, input().split()))

k = int(input())

# Edge case
if k > n:
    print("Invalid K")
else:

    # Step 1: Compute first window sum
    window_sum = 0
    i = 0

    while i < k:
        window_sum = window_sum + arr[i]
        i = i + 1

    max_sum = window_sum

    print("Initial Window Sum:", window_sum)

    # Step 2: Slide window
    left = 0
    right = k

    while right < n:

        # Remove left element
        window_sum = window_sum - arr[left]

        # Add right element
        window_sum = window_sum + arr[right]

        print("Window from index", left + 1, "to", right, "Sum:", window_sum)

        if window_sum > max_sum:
            max_sum = window_sum

        left = left + 1
        right = right + 1

    print("--------------------------")
    print("Maximum Subarray Sum of size", k, "=", max_sum)
    print("==========================")
    print("End of Program")
