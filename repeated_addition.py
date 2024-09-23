# multiplication via repeated addition
def repeated_addition_multiplication(num1, num2):
    result = 0
    for i in range(num2):
        result += num1
    return result