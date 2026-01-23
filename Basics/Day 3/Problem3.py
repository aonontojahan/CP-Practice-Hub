n = int(input())
digit_sum = 0

while n > 0:
    digit = n % 10
    digit_sum = digit_sum + digit
    n = n // 10

print(digit_sum)
