
# O(nlogn) time | O(n) Space
#square from right to left 
def sortedSquareArray(nums):
    
    start = 0
    end = len(nums) - 1
    output = [0] * (end + 1)
    index = end
    
    while end != start:
        left = abs(nums[start])
        right = abs(nums[end])
        
        if left < right:
            output[index] = right * right
            end -= 1
        else:
            output[index] = left * left 
            start += 1
            
        index -= 1  # continues to reduce regardless  
        
        if index == 0:
            output[index] = nums[end] * nums[start] # asigns the last index with whats left
            
        
    return output

if __name__ == "__main__":
    
    #numbers = [1, 2, 3, 5,6,8,9]
    numbers = [-7, -5, -4, 3, 6, 8, 9]
    rs = sortedSquareArray(numbers)
    print(rs)
    