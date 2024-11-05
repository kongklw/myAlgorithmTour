from itertools import count
from tarfile import data_filter
from xxlimited_35 import error


def bubble_sort(alist):
    # near two num compare ,the large swap the position
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


def select_sort(alist):
    # define
    # select the min(max) num store in the start(end) position

    for i in range(len(alist) - 1, 0, -1):

        max_index = 0
        for j in range(i):
            if alist[j] >= alist[max_index]:
                max_index = j
        alist[max_index], alist[i] = alist[i], alist[max_index]


class SingleNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        cur = self.__head

        while cur != None:
            cur = cur.next
            count += 1

        return count

    def travel(self):

        cur = self.__head
        while cur != None:
            print("cur data", cur.data)
            cur = cur.next
        print("")

    def add(self, data):
        node = SingleNode(data)

        node.next = self.__head
        self.__head = node

    def append(self, data):

        node = SingleNode(data)
        cur = self.__head
        while cur.next != None:
            cur = cur.next
        print(cur)
        cur.next = node

    def insert(self, data, position):

        node = SingleNode(data)

        length = self.length()
        if position >= length:
            raise Exception("exceed the length of link_list")
        if self.is_empty():
            self.add(data)
            return
        if position == 0:
            self.add(data)
            return
        if position == length - 1:
            self.append(data)
            return
        cur = self.__head
        count = 1
        while count < position:
            cur = cur.next
            count += 1

        next_node = cur.next

        cur.next = node
        node.next = next_node

    def remove(self, data):

        cur = self.__head
        pre = None

        while cur != None:

            if cur.data == data:
                if pre is None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, data):

        cur = self.__head

        while cur != None:
            if cur.data == data:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    alist = [1, 9, 3, 0, 2, 3, 1]

    # bubble_sort(alist)
    # quick_sort(alist, 0, len(alist) - 1)
    # select_sort(alist)
    # print(alist)

    link_list = SingleLinkList()
    for i in range(10):
        link_list.add(i)

    link_list.append(90)
    length = link_list.length()
    print(length)

    link_list.insert(20, 10)
    link_list.remove(3)


    link_list.travel()
