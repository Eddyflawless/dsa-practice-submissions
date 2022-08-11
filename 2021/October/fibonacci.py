def fib(n,memo):
    """
        0 1 1 2 3 5
    """
    if(n < 0) :
        return 0
    elif n == 1:
        return 1
    elif memo[n]:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)    
    
    return memo[n]

        
if __name__ == '__main__':

    """
        1 1 2 3 5 8 13
    """
    memo = []
    print(fib(5,memo))
    # print(memo)

    


    