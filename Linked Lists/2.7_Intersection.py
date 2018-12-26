#Intersection: Given two (singly) linked lists, determine if the two lists intersect.
#Return the intersecting node. Note that the intersection is defined based on reference, not value.That is,
#If the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked
#list, then they are intersecting.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def print(self):
        current = self.head
        while current != None:
            print(current.getData(), end=" ")
            if current.getNext() != None:
                print("-->", end=" ")
            current = current.getNext()
        print("\n")

    def intersection(self, l2):
        i = []
        cl1 = self.head
        cl2 = l2.head
        while cl1 != None and cl2 != None:
            if cl1.getData() == cl2.getData():
                i.append(cl1.getData())
                cl1 = cl1.getNext()
                cl2 = cl2.getNext()
            else:
                cl1 = cl1.getNext()
                cl2 = cl2.getNext()
        return i


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    a1 = input("Enter a string: ")
    a2 = input("Enter a string: ")
    for i in a1[::-1]:
        ll1.insert(i)
    for j in a2[::-1]:
        ll2.insert(j)
    intersection_node = ll1.intersection(ll2)
    for k in intersection_node:
        print(k, end=" ")
