def insertion_sort(element):
    total = 0
    for i in range(len(element)):
        # get running mean
        # total = total + element[i]
        # print(total/(i+1))
        for x in range(i):
            if element[i] < element[x]:
                element.insert(x,element.pop(i))
                break
        if i%2 ==0:
            index = i/2
            print(element[int(index)])
        else:
            index = i//2
            print((element[int(index)] + element[int(index)+1]) /2)
tests = [
        [2, 1, 5, 7, 2, 0, 5],
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        [2, 9, 7, 6, 4, 3, 8, 5]
    ]
            
for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
element = [11,9,29,7,2,15,28]

insertion_sort(element)
print(element)
# i =5
# for i in range(5):
#     print(i)