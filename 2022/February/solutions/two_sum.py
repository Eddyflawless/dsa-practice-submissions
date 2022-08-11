
#[2,1,5,3]

def main(nums, target): #returns an array of indexes of numbers that sum to target
    prev_map = {}
    for n in nums:
        diff = target - n  
        if diff in prev_map:
            return [ diff, n  ] 
        prev_map[n] = diff

    print(prev_map)
    return []

    

if __name__ == '__main__':
    sum_values = main(nums=[2,1,5,3], target=5)
    print("sum_values :", sum_values)
