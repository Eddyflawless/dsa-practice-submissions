# O(N) time | O(1) space
def solutionB(str):
    l = 0
    r = len(str)-1
    while l < r:
        if str[l] != str[r] :
            return False
        l += 1
        r -= 1   
         
    return True    
    

# O(N) time | O(N) space
def solutionA(str):
    
    reversedStr = str[::-1]
    print(reversedStr," | ", str)
    for index, s in enumerate(str):
        if s != reversedStr[index]:
            return False
            
    return True

if __name__ == "__main__":
    
    # str = 'abcdcdba' # is not a palidrome
    str = 'abcfcba' # is a palidrome
    
    if solutionB(str):
        print("is a palidrome")
    else:
        print("is not a palidrome")    
