first_number = 0
second_number = 1
n = int(input("Enter n: "))
if n < 0:
    print("Please enter a positive integer ")
elif n == 0:
    print("Fibonacci number (n) = ", first_number)
elif n == 1:
    print("Fibonacci number (n) = ", second_number)
else:
    for i in range(n-1):
        first_number, second_number = second_number, first_number+second_number
    print("Fibonacci number (n) = ", second_number)


