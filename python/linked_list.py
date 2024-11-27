class SingleNode(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


test_link_list = SingleNode(4, None)
test_link_list.next = SingleNode(2, None)
test_link_list.next.next = SingleNode(5, None)
print("hello world")

print("hahaha")