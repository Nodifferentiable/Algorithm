# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def rearrangedList(self, node):
    """
    :type node: ListNode
    :rtype: void
    """

    length = 0
    p = node
    while p != None:
      length += 1
      p = p.next

    if length <= 1:
      return node

    mid = length >> 1

    p1 = p2 = node

    for i in range(mid):
      p1 = p1.next

    p = p1  # 存下中间的那一个位置 作为 1-2/n节点 终点
    p3 = None

    # 逆置的头
    while p1 != None:
      tp = p1
      p1 = p1.next
      tp.next = p3
      p3 = tp
    # p3 是逆置之后n n-1 n-2 的头

    ans = node  # 答案node
    p2 = node.next  # p2是1号点 第一个点必选

    while p2 != p and p3 != None:
      # 选n
      ans.next = p3
      ans = p3
      p3 = p3.next

      # 选2
      ans.next = p2
      ans = p2
      p2 = p2.next

    while p2 != p:
      ans.next = p2
      ans = p2
      p2 = p2.next

    while p3 != None:
      ans.next = p3
      ans = p3
      p3 = p3.next
