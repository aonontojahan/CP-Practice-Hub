def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid integers.")

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        print("Program execution completed.")


divide_numbers()

print("End of the program.")
