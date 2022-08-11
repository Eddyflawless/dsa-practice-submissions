def biggest_number(arr, n, highest):
    if n < 1:
        return
    elif arr[n] > highest:
        #swap  values
        highest = arr[n]
        print(f" highest {highest}")
        biggest_number(arr, n -1, highest)       
    else:
        biggest_number(arr, n -1, highest)          

        

if __name__ == '__main__':
    items = [12,4,600, 3,1000, 9, 10, 1,9, 900]
    biggest_number(items, len(items)-1, 0)
