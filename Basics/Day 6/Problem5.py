n = int(input())

palindrome_count = 0
armstrong_count = 0
perfect_count = 0

while n > 0:

    num = int(input())
    original = num

    digit_count = 0
    sum_digits = 0
    reverse = 0

    temp = num

    # First pass: count digits
    temp1 = num
    while temp1 > 0:
        digit_count = digit_count + 1
        temp1 = temp1 // 10

    # Second pass: digit operations
    while temp > 0:

        digit = temp % 10

        sum_digits = sum_digits + digit
        reverse = reverse * 10 + digit

        temp = temp // 10

    print("Number:", original)
    print("Digit Count:", digit_count)
    print("Sum of Digits:", sum_digits)
    print("Reverse:", reverse)

    # Palindrome check
    if reverse == original:
        print("Palindrome: Yes")
        palindrome_count = palindrome_count + 1
    else:
        print("Palindrome: No")

    # Armstrong check
    temp2 = original
    armstrong_sum = 0

    while temp2 > 0:

        digit = temp2 % 10

        power = 1
        i = 1

        while i <= digit_count:
            power = power * digit
            i = i + 1

        armstrong_sum = armstrong_sum + power

        temp2 = temp2 // 10

    if armstrong_sum == original:
        print("Armstrong: Yes")
        armstrong_count = armstrong_count + 1
    else:
        print("Armstrong: No")

    # Perfect number check
    divisor = 1
    divisor_sum = 0

    while divisor < original:
        if original % divisor == 0:
            divisor_sum = divisor_sum + divisor
        divisor = divisor + 1

    if divisor_sum == original:
        print("Perfect: Yes")
        perfect_count = perfect_count + 1
    else:
        print("Perfect: No")

    print("----------------------------")

    n = n - 1

# Final Summary
print("====== FINAL REPORT ======")
print("Total Palindromes:", palindrome_count)
print("Total Armstrong Numbers:", armstrong_count)
print("Total Perfect Numbers:", perfect_count)
print("Program is over")