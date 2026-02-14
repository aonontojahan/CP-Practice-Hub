n = int(input())

arr = list(map(int, input().split()))

# Step 1: Create prefix array
prefix = [0] * n

prefix[0] = arr[0]

i = 1
while i < n:
    prefix[i] = prefix[i - 1] + arr[i]
    i = i + 1

# Debug print (optional understanding)
# print("Prefix:", prefix)

q = int(input())

query_number = 1

while q > 0:

    L, R = map(int, input().split())

    print("Query", query_number, ":")

    if L == 0:
        range_sum = prefix[R]
    else:
        range_sum = prefix[R] - prefix[L - 1]

    print("Sum from", L, "to", R, "=", range_sum)
    print("------------------------")

    query_number = query_number + 1
    q = q - 1
    
    print("Remaining Queries:", q)
