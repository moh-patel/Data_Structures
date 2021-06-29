element = [11,9,29,7,2,15,28]

size = len(element)
# i =0
# while(i<size-1):
#     if element[i] > element[i+1]:
#         tmp = element[i]
#         element[i] = element[i+1]
#         element[i+1]=tmp
#         print(element)
#     i+=1
    
# print(element) 
# size = len(element)
# s=1
# pivot = element[len(element)-s]

# for i in range(size -1):
#     p = element[i]
#     if p > 



def quicksort(element, start, end):
    if start < end:
        p = partition(element, start, end)
        quicksort(element, start, p-1)
        quicksort(element, p+1, end)

def partition(element, start, end):
    pivot = element[end]
    i = start
    j = start

    while(j < end):
        if element[j]< pivot:
            if i!= j:
                element[i], element[j] = element[j], element[i]
            i+=1
        j+=1
        print(element)
    element[i], element[end] = element[end], element[i]
    print('upon partition', element)
    print(f'i = {i}')
    return i

    # for j in range(start, end):
    #     if element[j] < pivot:
    #         element[i], element[j] = element[j], element[i]
    #         print(element)
    #         i+=1
    # element[i], element[end] = element[end], element[i]
    print('upon partition:', element)
    return i

if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        [2, 9, 7, 6, 4, 3, 8, 5]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quicksort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
# print(element)
# quicksort(element, 0, size-1)

# print(element)