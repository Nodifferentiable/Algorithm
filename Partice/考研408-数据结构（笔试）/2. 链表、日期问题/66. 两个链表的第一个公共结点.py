# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def findFirstCommonNode(self, headA, headB):
    """
    :type headA, headB: ListNode
    :rtype: ListNode
    """
    p1 = headA
    p2 = headB
    while p1 != p2:
      if p1 != None:
        p1 = p1.next
      else:
        p1 = headB
      if p2 != None:
        p2 = p2.next
      else:
        p2 = headA
    return p1
