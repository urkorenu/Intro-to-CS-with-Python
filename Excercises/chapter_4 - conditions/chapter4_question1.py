x = int(input("Enter x: "))
numerator = (x**2-1)*2
denominator = 2*x-6
result = numerator/(denominator**0.5)
if denominator == 0:
    print("Error: division by zero")
elif denominator < 0:
    print("Imaginary number")
else:
    print(result)
