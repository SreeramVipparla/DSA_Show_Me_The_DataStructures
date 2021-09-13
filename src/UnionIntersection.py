import math
# For this question i have referred the knowledge \
# post https://knowledge.udacity.com/questions/637444


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(linkedlist_1, linkedlist_2):
    union = LinkedList()
    new_union_set = set()
    node1 = linkedlist_1.head
    node2 = linkedlist_2.head

    while node1:
        new_union_set.add(node1.value)
        node1 = node1.next

    while node2:
        new_union_set.add(node2.value)
        node2 = node2.next

    for element in new_union_set:
        union.append(element)

    return union


def intersection(linkedlist_1, linkedlist_2):
    intersection = LinkedList()

    test_set_1 = set()
    test_set_2 = set()

    if linkedlist_2.head == None and linkedlist_1.head == None:
        return None

    intersection_set_1 = linkedlist_1.head
    while intersection_set_1 != None:
        test_set_1.add(intersection_set_1.value)
        intersection_set_1 = intersection_set_1.next

    intersection_set_2 = linkedlist_2.head
    while intersection_set_2 is not None:
        test_set_2 .add(intersection_set_2.value)
        intersection_set_2 = intersection_set_2.next

    combined_intersection_set = test_set_1.intersection(test_set_2)

    for i in combined_intersection_set:
        intersection.append(i)

        return intersection
    if len(combined_intersection_set) == 0:
        return None

# Edge Cases

# Edge case 1 
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

# Expected output
# None
# Edge case 2
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element_1 = [1, 2, 3]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

# Expected output
# 1 -> 2 -> 3 -> None
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Expected output
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 4 ->


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Expected output-
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> None
