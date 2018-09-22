class Node:
   def __init__(self, value, next=None):
        self.value = value
        self.next = next

some_list = Node(1, Node(2, Node(3, Node(4))))

def print_list(head, end='\n'):
    while head:
        print(head.value, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)

print_list(some_list)

def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print_list(reverse_list(some_list))