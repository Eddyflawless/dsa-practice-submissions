# O(n) time  | O( s + t) space
def isValidAnagram(s: str, t: str)->bool:
    
    s_map = {}
    t_map = {}
    
    if len(s) != len(t):
        return False
         
    for i in range(len(s)):
        
        if s[i] in s_map:
            s_map[s[i]] += 1
        else:
            s_map[s[i]] = 1     
            
        if t[i] in t_map:
            t_map[t[i]] += 1
        else:
            t_map[t[i]] = 1                
         
    for a in s_map:
        if s_map[a] != t_map[a]:
           return False  
    
    return True


if __name__ == '__main__':
    
    
    if isValidAnagram('anagratt','nagramat'):
        print ("Is valid anagram")
    else:
        print ("Not valid anagram")    
        