
def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product


result = calculate(10, 5)

print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
