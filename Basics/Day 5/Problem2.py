n = int(input())

palindrome_count = 0
strong_count = 0

while n > 0:

    num = int(input())
    original_num = num

    sum_digits = 0
    product_digits = 1
    digit_count = 0

    reverse_num = 0
    strong_sum = 0

    temp = num

    # Digit processing
    while temp > 0:
        digit = temp % 10

        sum_digits = sum_digits + digit
        product_digits = product_digits * digit
        digit_count = digit_count + 1

        reverse_num = reverse_num * 10 + digit

        # Factorial calculation
        fact = 1
        i = 1
        while i <= digit:
            fact = fact * i
            i = i + 1

        strong_sum = strong_sum + fact

        temp = temp // 10

    print("Number:", original_num)
    print("Sum of digits:", sum_digits)
    print("Product of digits:", product_digits)
    print("Digit count:", digit_count)

    # Palindrome check
    if original_num == reverse_num:
        print("Palindrome: Yes")
        palindrome_count = palindrome_count + 1
    else:
        print("Palindrome: No")

    # Strong number check
    if strong_sum == original_num:
        print("Strong Number: Yes")
        strong_count = strong_count + 1
    else:
        print("Strong Number: No")

    print("----------------------------")

    n = n - 1

# Final Summary
print("===== FINAL SUMMARY =====")
print("Total Palindromes:", palindrome_count)
print("Total Strong Numbers:", strong_count)
