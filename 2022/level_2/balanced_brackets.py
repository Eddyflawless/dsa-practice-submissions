openingBrackets = ['{', '[', '(']
closingBrackets = ['}', ']', ')']


def isAPair(opening, closing) -> bool:
    if openingBrackets.index(opening) == closingBrackets.index(closing):
        return True 
    return False
    

# O(n) time | O(n) space
def isBracketsBalanced(brackets) -> bool:
    mStack = []
    
    for bracket in brackets:
        if bracket in openingBrackets:
            mStack.append(bracket)
        elif bracket in closingBrackets:
           #it is a closing bracket 
            if len(mStack) != 0 :
                matchingPair = mStack.pop()
                if isAPair(matchingPair, bracket) is False:
                    break
        else:
            raise Exception("Unrecognized bracket of: " + bracket)
                                 
    if len(mStack) != 0:
        return False
    
    return True

if __name__ == '__main__':
    
    brackets = "(([]()()){})" #balanced
    # brackets = "(([]()()){}" #not balanced
    # brackets = "((}}[]" #not balanced
    # brackets = "#" # wrong and unbalanced | should throw an error
    
    if isBracketsBalanced(brackets):
        print(f"{brackets} is balanced")
    else:
        print(f"{brackets} is not balanced")