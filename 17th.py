# Merged 2 sorted list
def merged(list1,list2):
    result=[]
    while list1 and list2:
        if list1[0]<list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result+=list1
    result+=list2
    return result
print(merged([1,2,4],[1,3,4]))

#merged 2 list by linklist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next

# Helper functions to convert list -> linked list and linked list -> list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

sol = Solution()
l1 = list_to_linkedlist([1,2,4])
l2 = list_to_linkedlist([1,3,4])
merged = sol.mergeTwoLists(l1, l2)
print(linkedlist_to_list(merged))   # Output: [1, 1, 2, 3, 4, 4]

l3 = list_to_linkedlist([])
l4 = list_to_linkedlist([])
merged2 = sol.mergeTwoLists(l3, l4)
print(linkedlist_to_list(merged2))  # Output: []

l5 = list_to_linkedlist([])
l6 = list_to_linkedlist([0])
merged3 = sol.mergeTwoLists(l5, l6)
print(linkedlist_to_list(merged3))  # Output: [0]
