
print("********************  Q1  *************************")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle_node(head):
    if head is None or head.next is None:
        return None
    
    slow_ptr = head
    fast_ptr = head
    prev_ptr = None
    
    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next
    
    prev_ptr.next = slow_ptr.next
    return head

def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
    print()

# Example 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

print("Input:")
print_linked_list(head1)

new_head1 = delete_middle_node(head1)

print("Output:")
print_linked_list(new_head1)

# Example 2
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(5)
head2.next.next.next.next.next = Node(1)

print("Input:")
print_linked_list(head2)

new_head2 = delete_middle_node(head2)

print("Output:")
print_linked_list(new_head2)




print("\n********************  Q2  *************************\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_loop(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

# Create a linked list with a loop for testing
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next  # Creating a loop by connecting the last node to the second node

# Check if the linked list has a loop
has_loop_result = has_loop(head)

# Print the result
print(has_loop_result)




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

def is_palindrome(head):
    if head is None or head.next is None:
        return True

    slow_ptr = head
    fast_ptr = head

    # Find the middle of the linked list
    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Reverse the second half of the linked list
    second_half = reverse_linked_list(slow_ptr.next)
    slow_ptr.next = None

    # Compare the first half and reversed second half
    return compare_linked_lists(head, second_half)

def reverse_linked_list(head):
    prev_ptr = None
    curr_ptr = head

    while curr_ptr is not None:
        next_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr

    return prev_ptr

def compare_linked_lists(head1, head2):
    ptr1 = head1
    ptr2 = head2

    while ptr1 is not None and ptr2 is not None:
        if ptr1.data != ptr2.data:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1 is None and ptr2 is None

# Create the linked list
head1 = Node('R')
head1.next = Node('A')
head1.next.next = Node('D')
head1.next.next.next = Node('A')
head1.next.next.next.next = Node('R')

# Check if the linked list is a palindrome
is_palindrome_result1 = is_palindrome(head1)

# Print the result
print("Output:", "Yes" if is_palindrome_result1 else "No")

# Create another linked list
head2 = Node('C')
head2.next = Node('O')
head2.next.next = Node('D')
head2.next.next.next = Node('E')

# Check if the linked list is a palindrome
is_palindrome_result2 = is_palindrome(head2)

# Print the result
print("Output:", "Yes" if is_palindrome_result2 else "No")




print("\n********************  Q5  *************************\n")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def detect_and_remove_loop(head):
#     if head is None or head.next is None:
#         return

#     slow_ptr = head
#     fast_ptr = head

#     # Detect the loop in the linked list
#     while fast_ptr is not None and fast_ptr.next is not None:
#         slow_ptr = slow_ptr.next
#         fast_ptr = fast_ptr.next.next

#         if slow_ptr == fast_ptr:
#             break

#     # If loop exists, find the start of the loop
#     if slow_ptr == fast_ptr:
#         slow_ptr = head

#         while slow_ptr.next != fast_ptr.next:
#             slow_ptr = slow_ptr.next
#             fast_ptr = fast_ptr.next

#         # Remove the loop
#         fast_ptr.next = None

# def print_linked_list(head):
#     curr = head
#     while curr is not None:
#         print(curr.data, end=' ')
#         curr = curr.next
#     print()

# # Create a linked list with a loop for testing
# head1 = Node(1)
# head1.next = Node(3)
# head1.next.next = Node(4)
# head1.next.next.next = head1.next  # Creating a loop by connecting the last node to the second node

# print("Input:")
# print_linked_list(head1)

# # Remove the loop from the linked list
# detect_and_remove_loop(head1)

# print("Output:")
# print_linked_list(head1)

# # Create another linked list without a loop
# head2 = Node(1)
# head2.next = Node(8)
# head2.next.next = Node(3)
# head2.next.next.next = Node(4)

# print("Input:")
# print_linked_list(head2)

# # Remove the loop from the linked list
# detect_and_remove_loop(head2)

# print("Output:")
# print_linked_list(head2)


print("\n********************  Q6  *************************\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def retain_delete(head, M, N):
    if M == 0:
        return None

    curr_ptr = head
    prev_ptr = None

    while curr_ptr is not None:
        # Retain M nodes
        for _ in range(M):
            if curr_ptr is None:
                return head
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.next

        # Delete N nodes
        for _ in range(N):
            if curr_ptr is None:
                break
            curr_ptr = curr_ptr.next

        # Adjust the pointers
        prev_ptr.next = curr_ptr

    return head

def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
    print()

# Create a linked list for testing
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next.next = Node(8)

print("Input:")
print_linked_list(head1)

M = 2
N = 2

# Retain M nodes and delete N nodes
head1 = retain_delete(head1, M, N)

print("Output:")
print_linked_list(head1)


# Create another linked list for testing
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(4)
head2.next.next.next.next = Node(5)
head2.next.next.next.next.next = Node(6)
head2.next.next.next.next.next.next = Node(7)
head2.next.next.next.next.next.next.next = Node(8)
head2.next.next.next.next.next.next.next.next = Node(9)
head2.next.next.next.next.next.next.next.next.next = Node(10)

print("Input:")
print_linked_list(head2)

M = 3
N = 2

# Retain M nodes and delete N nodes
head2 = retain_delete(head2, M, N)

print("Output:")
print_linked_list(head2)



print("\n********************  Q7  *************************\n")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_alternate_positions(first, second):
    if second is None:
        return first

    curr_first = first
    curr_second = second

    while curr_first is not None and curr_second is not None:
        temp = curr_first.next
        curr_first.next = curr_second
        curr_second = curr_second.next
        curr_first.next.next = temp
        curr_first = temp

    # If second list has remaining nodes, append them to the end of the first list
    if curr_second is not None:
        curr_first.next = curr_second

    # Empty the second list
    second = None

    return first

def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
    print()

# Create the first linked list for testing
first = Node(5)
first.next = Node(7)
first.next.next = Node(17)
first.next.next.next = Node(13)
first.next.next.next.next = Node(11)

# Create the second linked list for testing
second = Node(12)
second.next = Node(10)
second.next.next = Node(2)
second.next.next.next = Node(4)
second.next.next.next.next = Node(6)

print("Input:")
print("First List:", end=' ')
print_linked_list(first)
print("Second List:", end=' ')
print_linked_list(second)

# Insert nodes of the second list into the first list at alternate positions
first = insert_at_alternate_positions(first, second)

print("Output:")
print("First List:", end=' ')
print_linked_list(first)
print("Second List:", end=' ')
print_linked_list(second)


print("\n********************  Q8  *************************\n")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_circular_linked_list(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Create a circular linked list for testing
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head

# Check if the linked list is circular
result = is_circular_linked_list(head)

if result:
    print("The linked list is circular.")
else:
    print("The linked list is not circular.")
