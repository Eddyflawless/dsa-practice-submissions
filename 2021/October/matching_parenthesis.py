def balancedBrackets(Str):
    # stack for storing opening brackets
    stack = []

    opening_parenthesis = ["{","(","["]
    closing_parenthesis = ["}",")","]"]

    # Loop for checking string 
    for char in Str:
        if char in opening_parenthesis:
            stack.append(char)
        elif char in closing_parenthesis:
            if len(stack) == 0:
                return False

            _p  = stack.pop() # get the last inserted parenthesis
            if not compare(_p, char):
                return False
            
    if len(stack) != 0 :
        return False

    return True


def compare(opening, closing):
    if opening == '{' and closing == '}':
        return True
    if opening == '['  and closing == ']':
        return True
    if opening == '(' and closing == ')':
        return True

    return False    




if __name__ == '__main__':
    
    # print(balancedBrackets("{123(456[.768])}{}"))
    print(balancedBrackets("{[]{()}}"))

   