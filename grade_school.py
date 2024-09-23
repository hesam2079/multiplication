def grade_school_multiplication_book_version(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    result = 0
    for i in range(len(num1_str)):
        for j in range(len(num2_str)):
            result += (10**( i + j )) * int(num1_str[i]) * int(num2_str[j])

    return result

def grade_school_multiplication_my_version(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    result = 0
    for i in range(len(num1_str) - 1, -1, -1):
        for j in range(len(num2_str) - 1, -1, -1):
            result += (10 ** ((len(num1_str) - 1 - i) + (len(num2_str) - 1 - j))) * int(num1_str[i]) * int(num2_str[j])

    return result