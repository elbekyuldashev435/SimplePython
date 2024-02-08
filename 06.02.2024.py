
""" Theme: Garbage collection """


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1
list_head = []
while head:
    list_head.append(head.value)
    head = head.next

new_reverse = list_head[::-1]
for i in new_reverse:
    print(i)

# list1 = [1, 2, 3]
# list2 = list1
# list1.append(4)
# print(list1,'\n',list2)
# print(id(list1))
# print(id(list2))
#
# print('---------------------------------')
#
# list3 = [1, 2, 3]
# list4 = list3.copy()
# list3.append(4)
# print(id(list3))
# print(id(list4))
# print(list3)
# print(list4)


