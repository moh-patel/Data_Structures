from math import ceil

def shell_sort(arr):
    
    size = len(arr)
    i = 0
    gap = size//2

    while gap > 0:
        i = 0
        while(i<size):
        # for i in range(0,size,gap):
            for x in range(0,i, gap):
                if arr[i] < arr[x]:
                    arr.insert(x,arr.pop(i))
                    break
                elif arr[i] == arr[x]:
                    arr.pop(i)
                    size = size-1
                    i-=1  
                    break
            i+=gap
        print(arr)
        gap-=1
    print(arr)

arr = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
arr2=[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
shell_sort(arr)
shell_sort(arr2)