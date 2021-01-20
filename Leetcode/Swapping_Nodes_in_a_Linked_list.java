/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

// two pointer 풀이
// O(n)

class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode left = head;
        ListNode right = head;
        
        int length = 0;
        while(left != null) {
            left = left.next;
            length++;
        }
        
        left = head;
        int l = k, r = length - k + 1;
        
        while(l-- > 1) left = left.next;
        while(r-- > 1) right = right.next;
        
        int temp = left.val;
        left.val = right.val;
        right.val = temp;
        
        return head;
    }
}