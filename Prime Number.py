x = int(input("Enter A Number"))

A= False

if x < 1:
        for i in range(2, x // 2):
            if (x % i) == 0:
                A=False
                break

if A:
    print("Its Not A Number ")
else:
    print("Its A PrimeNumber")