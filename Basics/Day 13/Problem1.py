print("Hello Everyone")
print("Practicing CP Day 13")
print("Practicing Recursion Related Problems")

def factorial(n):

    print("Calling factorial with:", n)

    # Base case
    if n == 0:
        print("Base case reached")
        return 1

    if n == 1:
        print("Base case reached")
        return 1

    # Recursive case
    result = n * factorial(n - 1)

    print("Returning:", result)

    return result


num = int(input())

answer = factorial(num)
print("Final Answer:", answer)
print("========================")
print("The factorial of", num, "is:", answer)
