n = int(input())
arr = list(map(int, input().split()))
target = int(input())

even_count = 0
odd_count = 0

# Even and Odd count
i = 0
while i < n:
    if arr[i] % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    i = i + 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)

# Maximum and Minimum
maximum = arr[0]
minimum = arr[0]

i = 1
while i < n:
    if arr[i] > maximum:
        maximum = arr[i]
    if arr[i] < minimum:
        minimum = arr[i]
    i = i + 1

print("Maximum:", maximum)
print("Minimum:", minimum)

# Duplicate count
duplicate_count = 0
visited = []

i = 0
while i < n:
    if arr[i] not in visited:
        count = 0
        j = 0
        while j < n:
            if arr[i] == arr[j]:
                count = count + 1
            j = j + 1

        if count > 1:
            duplicate_count = duplicate_count + 1

        visited.append(arr[i])

    i = i + 1

print("Duplicate Elements:", duplicate_count)

# Prime count
prime_count = 0

i = 0
while i < n:

    num = arr[i]

    if num < 2:
        pass
    else:
        is_prime = True
        divisor = 2

        while divisor < num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor = divisor + 1

        if is_prime:
            prime_count = prime_count + 1

    i = i + 1

print("Prime Count:", prime_count)

# Pair sum
pair_count = 0

i = 0
while i < n:
    j = i + 1
    while j < n:
        if arr[i] + arr[j] == target:
            print("Pair:", arr[i], arr[j])
            pair_count = pair_count + 1
        j = j + 1
    i = i + 1

print("Total Valid Pairs:", pair_count)
print("Total Unique Pairs:", pair_count // 2)
print("Total Distinct Pairs:", pair_count // 4)
print("Total Distinct Unique Pairs:", pair_count // 8)
