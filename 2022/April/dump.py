def removeElement(self, nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


#incomplete assignment
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening = ["(","[","{"]
        closing = [")","]","}"]
        
        for p in list(s):
            
            if p in opening:
                #its a opening parenthesis
                stack.append(p)
            else:
                #its a closing parenthesis
                if len(stack) != 0:  
                    v1 = stack.pop()
                    if closing.index(p) != opening.index(v1):
                        return False
                else:
                    stack.append(p)
       
                    
        print("lenght:", len(stack))   
        
        if len(stack) != 0:
            
            return False
        
        return True    


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)    