class Solution(object):
    def deleteNode(self, node):
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)
