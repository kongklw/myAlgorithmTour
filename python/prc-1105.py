import time


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):

        for j in range(i):

            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def quick_sort(alist, start, end):
    if start >= end:
        return

    cur1 = start
    cur2 = end
    mid = alist[cur1]
    while cur1 < cur2:

        while alist[cur2] >= mid and cur1 < cur2:
            cur2 -= 1
        alist[cur1] = alist[cur2]
        while alist[cur1] < mid and cur1 < cur2:
            cur1 += 1
        alist[cur2] = alist[cur1]
    alist[cur1] = mid
    quick_sort(alist, start, cur1 - 1)
    quick_sort(alist, cur1 + 1, end)


fib_map = {}
print(len(fib_map))

def fib(n):
    '''

    0 1 1 2 3 5
    :param n:
    :return:
    20:38
    '''
    search = fib_map.get(n)
    if search is not None:

        return search

    if n == 1:
        fib_map[1] = 0
        return 0
    elif n == 2:
        fib_map[2] = 1
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        fib_map[n] = result
        return result


def fib2(n):
    '''

    0 1 1 2 3 5
    :param n:
    :return:
    20:38
    '''

    if n == 1:

        return 0
    elif n == 2:

        return 1
    else:

        return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    alist = [3, 2, 9, 0, 1, 3, 2]
    # bubble_sort(alist)  # 2 min
    # quick_sort(alist, 0, len(alist) - 1)  # 9min
    print(alist)

    n = 30
    start = time.time()
    result = fib(n)
    end = time.time()
    print('fib1 total wast time: {}  result is {}'.format(end - start, result))

    result2 = fib2(n)
    end2 = time.time()
    print('fib2 total wast time: {}  result is {} '.format(end2 - end, result2))
    print('changdu wei', len(fib_map))
    print('fast time is ', end2 - end - end + start)
