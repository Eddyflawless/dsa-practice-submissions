
def convertToBinary(num):

    original = num
    bit = ""
    while num != 0:
    
        quotient = num // 2
        reminder = num % 2
        bit = str(reminder) + bit
        num = quotient

    print(f"{original} is ---> {bit}")   

    return bit 
    

if __name__ == '__main__':
    
    assert convertToBinary(255) == "11111111" 

    assert convertToBinary(25) == "11001"  #expect 11001

    assert convertToBinary(100) == "1100100" #expect 1100100