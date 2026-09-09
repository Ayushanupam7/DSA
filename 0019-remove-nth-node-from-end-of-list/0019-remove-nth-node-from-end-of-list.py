class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Count nodes
        current = head
        length = 0

        while current is not None:
            length += 1
            current = current.next

        # Step 2: If removing the first node
        if n == length:
            return head.next

        # Step 3: Reach the node before the target
        current = head

        for i in range(length - n - 1):
            current = current.next

        # Step 4: Skip the target node
        current.next = current.next.next

        return head


        #phele count kro nodes then 3 case postion fist, postion from end , postion middle and last print full node skipped target node
#COUNT
# ↓
#FIND PREVIOUS NODE
# ↓
#SKIP TARGET