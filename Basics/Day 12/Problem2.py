print("Starting the program...")
n = int(input())

weights = list(map(int, input().split()))

days = int(input())

# Search space
left = max(weights)
right = sum(weights)

answer = right

while left <= right:

    mid = (left + right) // 2

    print("Trying Capacity:", mid)

    required_days = 1
    current_load = 0

    i = 0
    while i < n:

        if current_load + weights[i] <= mid:
            current_load = current_load + weights[i]
        else:
            required_days = required_days + 1
            current_load = weights[i]

        i = i + 1

    print("Days Needed:", required_days)

    if required_days <= days:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

    print("------------------------")

print("Minimum Required Capacity:", answer)
print("========================")
print("The sum of these weights is:", sum(weights))
