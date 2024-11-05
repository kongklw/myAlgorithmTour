alist = [1, 2, 5, 9, 3, 0, 4]


class SortAlgorithm(object):

    def __init__(self):
        pass

    def bubble_sort(self, origin):
        for i in range(len(origin) - 1, 0, -1):
            for j in range(i):
                if origin[j] > origin[j + 1]:
                    origin[j], origin[j + 1] = origin[j + 1], origin[j]
                else:
                    pass

        print(origin)
        return origin

    def quick_sort(self, origin, left, right):

        # exit condition
        if left >= right:
            return

        cur1 = left
        cur2 = right
        mid = origin[cur1]

        while cur1 < cur2:

            while cur1 < cur2 and origin[cur2] > mid:
                cur2 -= 1
            origin[cur1] = origin[cur2]

            while cur1 < cur2 and origin[cur1] < mid:
                cur1 += 1

            origin[cur2] = origin[cur1]
        origin[cur1] = mid
        print(origin)
        self.quick_sort(origin, left, cur1-1)
        self.quick_sort(origin, cur1+1, right)



s = SortAlgorithm()
# s.bubble_sort(alist)
s.quick_sort(alist, 0, len(alist) - 1)
