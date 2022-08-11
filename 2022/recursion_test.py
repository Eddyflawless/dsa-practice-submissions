

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

   

if __name__ == "__main__":

    test_cases = [
        [71,5,0,12,51,9,45],
    ]

    for arr in test_cases:
        merge_sort2(arr)
        print_list(arr)
