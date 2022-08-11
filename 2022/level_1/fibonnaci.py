from typing import Dict


def fib(n, memo): # pass by reference
    
    if n < 0:
        raise ValueError("n must be positive")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n in memo:
        #print("returning value from memo %d" % n)
        return memo[n]   
    
    result = fib(n-1,memo) + fib(n-2, memo)
    memo[n] = result
    return result

if __name__ == '__main__':

    # 0 1 1 2 3 5 8 13 21 34 45 ... Start counting from 1
    memo: Dict[int, int] = {}

    print("Nth number is: " , fib(9,memo) )    
    #print("memo is: " , memo )