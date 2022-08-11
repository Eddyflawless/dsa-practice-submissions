
def num_ways_one(stairs):
    one, two = 1, 1
    
    for i in range(stairs-2):
        temp = one
        one = one + two
        two = one
    
    return one

def num_ways_two(stairs):

    if stairs == 0 or stairs == 1:
        return 1
    else:
        print("n-1",stairs-1)
        print("n-2",stairs-2)
        return num_ways_two(stairs-1) + num_ways_two(stairs-2)    

def factorial(n):

    if n <= 1: return 1

    return n * factorial(n-1)        


if __name__ == '__main__':
    numer_of_pos = num_ways_two(5)
    print( "Number of possibility steps is %2d" % (numer_of_pos))


    f1 = factorial(3 )
    print("factorial %2d" % (f1))

