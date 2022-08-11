
def merge_sort(arr):
    
    print(f"length of arr: {arr}")
    
    if len(arr) > 1: # base case | so it stops when arr has only one item
        
        #divide
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]

        print("arr", arr)
        print("left: ",left_arr)
        print("right: ",right_arr)

        #conquer
        merge_sort(left_arr)
        merge_sort(right_arr)

        print("peek leftarray =>", left_arr)
        print("peek rightarray =>", right_arr)

        i = j = k = 0

        #combine
        while i < len(left_arr) and  j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1    

        while i  < len(left_arr):
            arr[k] = left_arr[i]
            i += 1 
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1




if __name__ == '__main__':
    items = [6,5,12,10,9,1]
    print("unsorted items", items)
    merge_sort(items)
    print("sorted: ", items)
    