from typing import Sequence, List, Dict
    
def firstDuplicateA(numbers: Sequence) -> int:
    
    cache:Dict[int,int] = {}
    
    for index, a in enumerate(numbers):
        # print(a,index)
        if a in cache:
            return index
        else:    
            cache[a] = True
    
    return -1    
    

if __name__ == '__main__':
    
    numbers: List[int] = [2,4,5,2,3,3,4]
    
    duplicateIndex:int = firstDuplicateA(numbers)
    
    if duplicateIndex != -1:
        
        print("first duplicate is ", numbers[duplicateIndex])
        
    else:
        print("no duplicate is ")
    