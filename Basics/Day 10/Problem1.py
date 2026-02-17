n = int(input())

arr = list(map(int, input().split()))

k = int(input())

prefix_sum = 0
count = 0

# Dictionary to store frequency of prefix sums
freq = {}

# Important: prefix sum 0 appears once
freq[0] = 1

i = 0

while i < n:

    prefix_sum = prefix_sum + arr[i]

    print("Index:", i)
    print("Current Element:", arr[i])
    print("Prefix Sum:", prefix_sum)

    required = prefix_sum - k

    if required in freq:
        count = count + freq[required]
        print("Found subarray(s) ending here")

    # Update frequency map
    if prefix_sum in freq:
        freq[prefix_sum] = freq[prefix_sum] + 1
    else:
        freq[prefix_sum] = 1

    print("Frequency Map:", freq)
    print("----------------------------")

    i = i + 1

print("Total Subarrays with Sum", k, "=", count)
print("==========================")
