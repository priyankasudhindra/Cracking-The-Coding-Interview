#Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all
#nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the
#elements less than x. The partition element x can appear anywhere in the "right partition";
#it does not need to appear between the left and right partitions.

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

    def partition(self, p):
        current = self.head
        lower = []
        higher = []
        while current != None:
            if current.getData() < p:
                lower.append(current.getData())
                current = current.getNext()
            else:
                higher.append(current.getData())
                current = current.getNext()
        res = LinkedList()
        for i in higher:
            res.insert(i)
        for j in lower:
            res.insert(j)
        return res

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
    l = [3, 5, 8, 5, 10, 2, 1]
    for i in l:
        myList.insert(i)
    p = int(input("Enter the partition element: "))
    res = myList.partition(p)
    res.print()

