
# O(n) time | O(n) space
def wordPattern(pattern: str, txt: str):
    
    txt_list =  txt.split()

    hash_map = {}
    
    if len(pattern) != len(txt_list):
        return False
    
    for i in range(len(pattern)):
        
        if pattern[i] in hash_map:
            if hash_map[pattern[i]] != txt_list[i]:
                return False
        else:
            hash_map[pattern[i]] = txt_list[i]
                
    return True

# O(n) time  | O( n + m) space
def wordPattern2(pattern: str, txt_list: str):
    pass


if __name__ == '__main__':
    
    if wordPattern("abba","dog cat cat dog"):
        print("Is a valid pattern")
    else:
        print("Is not a valid pattern")    