def fibonacci_numbers(count):
    fib_list = []
    a, b = 1, 1
    for _ in range(count):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


count_numbers = int(input())
result = fibonacci_numbers(count_numbers)
print(result)