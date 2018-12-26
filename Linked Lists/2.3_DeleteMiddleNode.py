#Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
#not necessarily the exact middle) of a singly linked list, given only access to that node.

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

    def deleteMiddleNode(self, node):
        current = self.head
        found = False
        previous = None
        while current != None:
            if current.getData() == node and previous == None:
                print("Cannot delete the first element!")
                found = True
                break
            elif current.getData() == node and current.getNext() == None:
                print("Cannot delete the last element!")
                found = True
                break
            elif current.getData() == node and previous != None and current.getNext() != None:
                previous.setNext(current.getNext())
                found = True
                print("Node " + str(node) + " successfully deleted!")
                break
            else:
                previous = current
                current = current.getNext()
        if found == False:
            print("Element to be deleted not found!")

    def print(self):
        current = self.head
        while current != None:
            print(current.getData(), end=" ")
            if current.getNext() != None:
                print("-->", end=" ")
            current = current.getNext()
        print("\n")


if __name__ == "__main__":
    myList = LinkedList()
    l = [33, 56, 34, 89, 20, 13, 5, 79]
    for i in l:
        myList.insert(i)
    myList.deleteMiddleNode(20)
    myList.print()
