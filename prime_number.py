def isprime(n:int):
    while n%2 == 0:
        print(2)
        n = n/2
    for i in range(3,int(n)):
        if n%i == 0:
            print(i)
        n = n/i






isprime(12)
            
