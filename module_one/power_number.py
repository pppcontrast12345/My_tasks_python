# User input
input_numbers = list(map(int, input("Enter numbers separated with comma: ").split(", ")))

# Generating a list with results
exponents_result = [num**exp for exp, num in enumerate(input_numbers)]

# Output the result
for num, result in zip(input_numbers, exponents_result):
    print(f"{num} of degree {exponents_result.index(result)} is {result}")