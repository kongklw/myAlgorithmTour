from pyasn1_modules.rfc2985 import randomNonce


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def quick_sort(alist, left, right):
    # exit condition
    if left >= right:
        return

    cur1 = left
    cur2 = right

    mid = alist[cur1]

    while cur1 < cur2:

        while alist[cur2] >= mid and cur1 < cur2:
            cur2 -= 1
        alist[cur1] = alist[cur2]

        while alist[cur1] <= mid and cur1 < cur2:
            cur1 += 1

        alist[cur2] = alist[cur1]

    alist[cur1] = mid

    quick_sort(alist, left, cur1 - 1)
    quick_sort(alist, cur1 + 1, right)


def select_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        max_index = i
        max_num = alist[max_index]
        for j in range(0, i):
            if alist[j] > max_num:
                max_index = j
                max_num = alist[j]
            else:
                pass
            print('this time i is {} j is {} and max_index is {} and max_num is {}'.format(i, j, max_index, max_num))
        if max_index != i:
            print('has swap')
            alist[i], alist[max_index] = alist[max_index], alist[i]
        else:

            print('no swap')
        print(alist)


def insert_sort(alist):
    for i in range(len(alist) - 1):

        for j in range(i + 1, 0, -1):
            print(i, '-----', j)
            # if alist[j]>
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


alist = [3, 8, 1, 2]

# bubble_sort(alist)
# quick_sort(alist, 0, len(alist) - 1)
# select_sort(alist)

insert_sort(alist)
print(alist)
