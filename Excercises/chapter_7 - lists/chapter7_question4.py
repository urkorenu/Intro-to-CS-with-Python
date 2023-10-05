# Finding all prime number up to n 
n = int(input("Enter n: "))
prime_list = []
is_prime = True
if n <= 1:
    print("Please enter a number that greater then 1 ")
else:
    for j in range(2,n+1):
        for i in range(2,int(j**0.5) + 1 ):
            if j%i == 0:
                is_prime = False
        if is_prime:
            prime_list.append(j)
        is_prime = True
print(prime_list)