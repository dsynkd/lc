class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode a = null;
        ListNode b = null;
        ListNode c = head;
        while(c != null) {
            b = c.next;
            c.next = a;
            a = c;
            c = b;
        }
        return a;
    }
}
