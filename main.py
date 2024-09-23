import repeated_addition
from repeated_addition import repeated_addition_multiplication
from grade_school import grade_school_multiplication_book_version, grade_school_multiplication_my_version
from karatsuba import karatsuba_multiplication_book_version
from karatsuba import karatsuba_multiplication_my_version
import time
import matplotlib.pyplot as plt

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("repeated addition: ", repeated_addition_multiplication(number1, number2))
print("grade school book version: ", grade_school_multiplication_book_version(number1, number2))
print("grade school my version: ", grade_school_multiplication_my_version(number1, number2))
print("karatsuba book version: ", karatsuba_multiplication_book_version(number1, number2))
print("karatsuba my version: ", karatsuba_multiplication_my_version(number1, number2))