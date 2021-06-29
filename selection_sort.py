def selection_sort(arr):
    size = len(arr)
    pos = 0
    for i in range(size):
        for x in range(pos,size):
            if arr[x] < arr[pos]:
                arr[x],arr[pos] = arr[pos], arr[x] 
        pos +=1
    
arr = [78, 12, 15, 8, 61, 53, 23, 27]

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)