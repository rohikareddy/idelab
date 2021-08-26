def is_prime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count=count+1
    if(count>1):
        print("not a prime number")
    else:
        print("prime number")
n=int(input())
is_prime(n)