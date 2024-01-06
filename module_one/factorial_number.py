def factorial_number(digit):
    result = 1
    if digit > 0:
        for i in range(1, digit + 1):
            result *= i
        return result
    else:
        return "Enter a positive number"


some_number = int(input())
final_result = factorial_number(some_number)
print(final_result)