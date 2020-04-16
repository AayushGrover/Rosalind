def fib(n,k):
    if n == 1 or n == 2: 
        return 1
    return fib(n-1, k) + k*fib(n-2, k)
        

if __name__ == "__main__":
    n, k = 35, 5
    print(fib(n,k))