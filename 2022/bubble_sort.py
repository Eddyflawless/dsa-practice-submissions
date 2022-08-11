
def bubble_sort(arr):
    arr_length = len(arr)
    for j in range(arr_length - 1):

        for i in range(arr_length - 1 - j):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp

def bubble_sort_a(arr, key="transaction_amount"):

    size = len(arr)

    for j in range(size-1):
        for i in range(size - 1 - j):
            
            if arr[j][key] > arr[j+1][key]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


if __name__ == "__main__":    
    # elements = [5,9,2,1,67,43,88,34]   
    # bubble_sort(elements)
    elements = [
        { 'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'}, 
        { 'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        { 'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'}
    ]
    bubble_sort_a(elements)
    print(elements)
