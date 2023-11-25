# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def filterList(self, head):
    vis = set()
    res = head
    vis.add(abs(res.val))

    while head.next != None:
      if abs(head.next.val) in vis:
        if head.next.next == None:
          head.next = None
        else:
          head.next = head.next.next
      else:head = head.next
      vis.add(abs(head.val))

    return res

    """
    :type head: ListNode
    :rtype: ListNode
    """
