def sum(n):
    if n ==1:
        return n
    return n + sum(n-1)


if __name__ == '__main__':
    tests = [
        1,2,3,4,5,6
    ]
    for num in tests:
        print(sum(num))