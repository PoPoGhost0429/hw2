class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    #iterator definition line 23-33
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next
            return node

    def get_at_index(self, index):
        current_node = self.head
        for i in range(index):
            if current_node is None:
                return None  # 索引超出範圍
            current_node = current_node.next
        return current_node

    def delete_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("\n",end='')

# 使用範例
data = []

with open("hw2_test.txt", "r") as file: # 逐行讀取文件
    for line in file:
        data.append(line.strip())

data.reverse()
n = int(input())

for i in range(n):
    A = DoublyLinkedList()
    B = []
    C = DoublyLinkedList()
    delNode = []
    
    temp = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print("A: ",end="")
    for ele in temp:
        A.append(ele)
    
    #output via iterator
    for node in A:
        print(node.data, end=" ")
    print("\n",end="")
    
    print("C: ",end="")
    for ele in B:
        C.append(A.get_at_index(ele-1).data)
        delNode.append(A.get_at_index(ele-1))
    
    for node in delNode:
        A.delete_node(node)
    
    A.reverse()  
    for node in A:
        C.append(node.data)
        
    #output via iterator
    for node in C:
        print(node.data, end=" ")
    print("\n")

