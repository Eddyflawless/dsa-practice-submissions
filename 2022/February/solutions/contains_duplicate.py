
"""
    Time: O(n) because we scanned through the array
    Memory: O(n) because of the hash map
"""

def contains_duplicate_01(nums):

    hash_map={}
    for v in nums:
        #does value exist in hash map
        if v in hash_map:
            return True
        else:
            hash_map[v] = True

    return False

""" 
    Time: O(n*2)
    Memory: O(1)

"""
def contains_duplicate_02(nums):

    i,k = 0, 1
    length = len(nums)
    while i < length:

        while k < length:
            if nums[i] == nums[k]:
                return True
            k += 1   

        i += 1   
        k = i + 1  

    return False
    
""" 


"""
def contains_duplicate_03(nums):

    nums = sort(nums)

    length = len(nums)

    for i in range(length):
        k = i + 1
        if k < length:
            if nums[i] == nums[k]:
                print(nums[i])
                return True

    return False


def sort(nums):

    i,k = 0, 1
    length = len(nums)

    while i < length:

        while k < length:

            if nums[i] > nums[k]:
                _t = nums[i]
                nums[i]  = nums[k]
                nums[k] = _t

            k += 1    


        i += 1
        k = i + 1

    return nums  

if __name__ == '__main__':
    # nums = [7,1,5,3,6,1,4,56,12,9]
    nums = [1,2,3,4,11,45,100,12,41]

    # output = contains_duplicate_01(nums)
    # output = contains_duplicate_02(nums)
    output = contains_duplicate_03(nums)
    sort(nums)
    
    if output:
        print("contains duplicates")
    else:
        print("doesnot contain duplicates")
