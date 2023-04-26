# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dum = prev = ListNode(None)

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if not list1:
            prev.next = list2
        elif not list2:
            prev.next = list1
        return dum.next


solution = Solution()
print(solution.mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))

assert solution.mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]) == [
    1, 1, 2, 3, 4, 4]
assert solution.mergeTwoLists(list1=[], list2=[]) == []
assert solution.mergeTwoLists(list1=[], list2=[0]) == [0]
