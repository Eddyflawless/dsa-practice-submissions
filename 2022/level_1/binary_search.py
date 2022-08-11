def binarySearchHelper(num, target,l,r):
    
    if l > r :
        return -1
    
    mIndex = (l + r) // 2
        
    if num[mIndex] == target:
        return mIndex
    
    # mIndex + 1 | mIndex + 1 to skip or exclude the middle value
    if num[mIndex] > target:
        return binarySearchHelper(num, target, l, mIndex - 1)
    else:
        return binarySearchHelper(num, target, mIndex + 1, r)

def binarySearch_a(nums, target):
    return binarySearchHelper(nums, target, 0, len(nums) - 1)

def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1
        
    mIndex = (l + r ) // 2
        
    while l <= r:
        
        if nums[mIndex] == target:
            return mIndex
        
        if nums[mIndex] > target:
            return binarySearch(nums[ : mIndex - 1],target)
        else:
            return binarySearch(nums[ mIndex + 1 : ],target)
    
    return  -1   


if __name__ == '__main__':
    
    heap = [0,1,21,33,45,46,61,71,72,73] # list has to be sorted
    print(binarySearch(heap, 33))
 