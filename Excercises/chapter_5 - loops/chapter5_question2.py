n = int(input("Enter n: "))
is_prime = True
if n <= 1:
    print("Please enter a number that greater then 1 ")
else:
    for i in range(2,n):
        if n%i == 0:
            is_prime = False
            break
        else:
            break
print("Result: ", is_prime)