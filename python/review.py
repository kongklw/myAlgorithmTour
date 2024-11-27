'''
this is an algorithm review file
daily refresh
'''


# 1.bubble sort
# 2.quick sort
# 3.single list
# 4.tree basic


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
    mid = alist[start]

    while cur1 < cur2:

        while alist[cur2] > mid and cur1 < cur2:
            cur2 -= 1
        while alist[cur1] < mid and cur1 < cur2:
            cur1 += 1
        alist[cur1], alist[cur2] = alist[cur2], alist[cur1]

    alist[cur1] = mid

    quick_sort(alist, start, cur1 - 1)
    quick_sort(alist, cur1 + 1, end)


if __name__ == '__main__':
    alist = [3, 1, 2, 8, 0, 5]
    # bubble_sort(alist) # 2min
    quick_sort(alist, 0, len(alist) - 1) # 8min
    print(alist)
    print("hello world")

