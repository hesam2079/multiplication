def karatsuba_multiplication_book_version(num1, num2):
    n = len(str(num1))
    if n < 4:
        return num1*num2
    else:
        m = n // 2
        x1 = num1 // 10**m
        x2 = num1 % 10**m
        y1 = num2 // 10**m
        y2 = num2 % 10**m

        a = karatsuba_multiplication_book_version(x1, y1)
        b = karatsuba_multiplication_book_version(x1 + x2, y1 + y2)
        c = karatsuba_multiplication_book_version(x2, y2)

        return (10**n - 10**m) * a + 10**m * b + (1 - 10**m) * c

def karatsuba_multiplication_my_version(num1, num2):
    n = len(str(num1))
    if n < 4:
        return num1*num2
    else:
        m = n // 2
        x1 = num1 // 10**m
        x2 = num1 % 10**m
        y1 = num2 // 10**m
        y2 = num2 % 10**m

        z0 = karatsuba_multiplication_my_version(x2, y2)
        z1 = karatsuba_multiplication_my_version(x1 + x2, y1 + y2)
        z2 = karatsuba_multiplication_my_version(x1, y1)

        return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0