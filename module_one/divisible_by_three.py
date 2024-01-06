def num_divisible_by_3(num):
    if num % 3 == 0:
        return "This number is divisible by 3"
    return "This number is not divisible by 3"


current_number = int(input("Enter an integer: "))
result = num_divisible_by_3(current_number)
print(result)