
print("********************  Q1  *************************")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_new_linked_list(list1, list2):
    if list1 is None and list2 is None:
        return None

    head = None
    tail = None

    while list1 is not None and list2 is not None:
        if list1.data >= list2.data:
            new_node = Node(list1.data)
            list1 = list1.next
        else:
            new_node = Node(list2.data)
            list2 = list2.next

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    # Add remaining nodes from list1
    while list1 is not None:
        new_node = Node(list1.data)
        tail.next = new_node
        tail = new_node
        list1 = list1.next

    # Add remaining nodes from list2
    while list2 is not None:
        new_node = Node(list2.data)
        tail.next = new_node
        tail = new_node
        list2 = list2.next

    return head

def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
    print()

# Create the first linked list for testing
list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)

# Create the second linked list for testing
list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)

print("Input:")
print("List 1:", end=' ')
print_linked_list(list1)
print("List 2:", end=' ')
print_linked_list(list2)

# Create a new linked list using list1 and list2
new_list = create_new_linked_list(list1, list2)

print("Output:")
print("New List:", end=' ')
print_linked_list(new_list)


# Create another set of linked lists for testing
list3 = Node(2)
list3.next = Node(8)
list3.next.next = Node(9)
list3.next.next.next = Node(3)

list4 = Node(5)
list4.next = Node(3)
list4.next.next = Node(6)
list4.next.next.next = Node(4)

print("Input:")
print("List 1:", end=' ')
print_linked_list(list3)
print("List 2:", end=' ')
print_linked_list(list4)

# Create a new linked list using list3 and list4
new_list = create_new_linked_list(list3, list4)

print("Output:")
print("New List:", end=' ')
print_linked_list(new_list)




print("\n********************  Q2  *************************\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Create the linked list for testing
head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

print("Input:")
print("Linked List:", end=' ')
print_linked_list(head)

# Remove duplicates from the linked list
head = remove_duplicates(head)

print("Output:")
print("Linked List:", end=' ')
print_linked_list(head)

# Create another linked list for testing
head = Node(10)
head.next = Node(12)
head.next.next = Node(12)
head.next.next.next = Node(25)
head.next.next.next.next = Node(25)
head.next.next.next.next.next = Node(25)
head.next.next.next.next.next.next = Node(34)

print("Input:")
print("Linked List:", end=' ')
print_linked_list(head)

# Remove duplicates from the linked list
head = remove_duplicates(head)

print("Output:")
print("Linked List:", end=' ')
print_linked_list(head)



print("\n********************  Q3  *************************\n")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_nth_node_from_end(head, n):
    if head is None:
        return None

    slow_ptr = head
    fast_ptr = head

    # Move the fast pointer ahead by n nodes
    for _ in range(n):
        if fast_ptr is None:
            return None
        fast_ptr = fast_ptr.next

    # Move both pointers until the fast pointer reaches the end
    while fast_ptr is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    return slow_ptr.data

# Create the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

# Find the Nth node from the end
N = 2
nth_node = find_nth_node_from_end(head, N)

# Print the result
print(nth_node)


print("\n********************  Q4  *************************\n")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_alternate_k_nodes(head, k):
    if head is None or k <= 1:
        return head

    # Helper function to reverse a linked list
    def reverse_list(node, count):
        prev = None
        curr = node
        while curr is not None and count > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count -= 1
        node.next = curr  # Connect the reversed group to the next group
        return prev

    current = head
    count = 0

    # Traverse the list to the start of the next group
    while current is not None and count < k:
        current = current.next
        count += 1

    # Reverse every alternate group of size k
    if count == k:
        # Reverse the current group
        new_head = reverse_list(head, k)

        # Skip the next group of size k
        count = 0
        while count < k and current is not None:
            current = current.next
            count += 1

        # Connect the reversed group to the next reversed group
        if current is not None:
            head.next = reverse_alternate_k_nodes(current, k)

        return new_head
    else:
        # If there are less than k nodes remaining, no need to reverse
        return head

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Create the linked list for testing
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

print("Input:")
print("Linked List:", end=' ')
print_linked_list(head)

# Reverse every alternate 3 nodes in the linked list
k = 3
new_head = reverse_alternate_k_nodes(head, k)

print("Output:")
print("Linked List:", end=' ')
print_linked_list(new_head)



print("\n********************  Q5  *************************\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_last_occurrence(head, key):
    if head is None:
        return head

    last_occurrence = None
    prev_last_occurrence = None
    current = head
    prev = None

    while current is not None:
        if current.data == key:
            last_occurrence = current
            prev_last_occurrence = prev

        prev = current
        current = current.next

    if last_occurrence is not None:
        if prev_last_occurrence is not None:
            prev_last_occurrence.next = last_occurrence.next
        else:
            head = last_occurrence.next

    return head

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Create the linked list for testing
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(10)

print("Input:")
print("Linked List:", end=' ')
print_linked_list(head)

# Delete the last occurrence of key from the linked list
key = 2
new_head = delete_last_occurrence(head, key)

print("Output:")
print("Linked List:", end=' ')
print_linked_list(new_head)



print("\n********************  Q6  *************************\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    if head is None:
        return None

    current = head
    while current is not None:
        # Swap the next and prev pointers of the current node
        temp = current.prev
        current.prev = current.next
        current.next = temp

        # Move to the next node (previously the prev node)
        current = current.prev

    # Update the head to the last node
    head = temp.prev

    return head

def print_doubly_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Create the original doubly linked list
head = Node(10)
head.next = Node(8)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next

print("Original Linked list:", end=' ')
print_doubly_linked_list(head)

# Reverse the doubly linked list
reversed_head = reverse_doubly_linked_list(head)

print("Reversed Linked list:", end=' ')
print_doubly_linked_list(reversed_head)



print("\n********************  Q7  *************************\n")
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    if head is None:
        return None

    current = head
    while current is not None:
        # Swap the next and prev pointers of the current node
        temp = current.prev
        current.prev = current.next
        current.next = temp

        # Move to the next node (previously the prev node)
        current = current.prev

    # Update the head to the last node
    head = temp.prev

    return head

def print_doubly_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Create the original doubly linked list
head = Node(10)
head.next = Node(8)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next

print("Original Linked list:", end=' ')
print_doubly_linked_list(head)

# Reverse the doubly linked list
reversed_head = reverse_doubly_linked_list(head)

print("Reversed Linked list:", end=' ')
print_doubly_linked_list(reversed_head)




print("\n********************  Q8  *************************\n")
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_node(head, position):
    if head is None:
        return None

    # Case 1: Delete the head node
    if position == 1:
        next_node = head.next
        if next_node is not None:
            next_node.prev = None
        head = next_node
        return head

    current = head
    count = 1

    # Traverse to the node at the given position
    while current is not None and count < position:
        current = current.next
        count += 1

    # Case 2: Delete node in the middle
    if current.next is not None:
        current.next.prev = current.prev

    current.prev.next = current.next

    # Case 3: Delete the last node
    if current.next is None:
        current.prev.next = None

    return head

def print_doubly_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Create the doubly linked list
head = Node(1)
head.next = Node(5)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next
head.next.next.next = Node(9)
head.next.next.next.prev = head.next.next

print("Original Linked list:", end=' ')
print_doubly_linked_list(head)

# Delete node at position 3
position = 3
head = delete_node(head, position)

print("Linked list after deletion:", end=' ')
print_doubly_linked_list(head)
