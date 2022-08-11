

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def merge_sort2(arr):
    if len(arr) <= 1:
        return arr

    #find mid of the array
    mid = len(arr)//2 #gets the integer number

    left = arr[:mid]
    right = arr[mid:]

    merge_sort2(left)
    merge_sort2(right)

    i = j = k = 0

    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    #check if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1            

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2 #gets the integer number

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)   
    right = merge_sort(right) 

    return sort_two_arrays(left,right)

def sort_two_arrays(a1,a2):
    sorted_list = []
    len_a1 = len(a1)
    len_a2 = len(a2)
    i = j = 0

    while i < len_a1 and j < len_a2:
        if  a1[i] <= a2[j]:
            sorted_list.append(a1[i])
            i += 1
        else:
            sorted_list.append(a2[j])
            j += 1    

    return sorted_list

if __name__ == "__main__":

    test_cases = [
        [71,5,0,12,51,9,45],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    print(set(1,1,2,34,3))
    for arr in test_cases:
        print("------------------------")
        print("Given array is", end="\n")
        print_list(arr)
        merge_sort2(arr)
        print("Sorted array is: ", end="\n")
        print_list(arr)
