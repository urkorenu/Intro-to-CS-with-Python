# works only on int and not on float.
# doesnt work on base 16
# b = base

def base_convertor_to_decimal(num : int, b : int) -> int:
        i   = 0
        res = 0
        while num > 0:
            a = num % 10
            res += (a*b**i)
            num //= 10
            i += 1
        return res
# print(base_convertor_to_decimal(51, 8))

def base_convertor_from_decimal(num : int, b : int) -> int:
        a   = num
        res = []
        while a > 0:
            if a == 1:
                res.append(1)
                break
            else:
                res.append(a%b)
            a = a // b
        number = 0
        res.reverse()
        for current_digit in res:
            number = number*10 + current_digit
        return number

print(base_convertor_from_decimal(41, 8))

# Edit funciton calls to print the binary and decimal number
# add shift left\right function. shift left = *2, shift right = / 2