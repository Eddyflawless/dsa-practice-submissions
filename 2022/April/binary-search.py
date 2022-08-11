def binary_search(items, l, r, x):

    if r >= l:
        mid= (r + l ) // 2

        # print(f"mid: {mid}")

        if items[mid] == x:
            return mid

        elif items[mid] < x:
            return binary_search(items, l, mid-1, x)    

        else:
            return binary_search(items, mid + 1, r, x)    

    else:
        return -1    



if __name__ == '__main__':
    items = [2, 3, 4, 10, 40]
    needle = 10
    result = binary_search(items, 0, len(items) - 1, needle)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
