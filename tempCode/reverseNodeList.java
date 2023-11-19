import java.util.List;

public class reverseNodeList {
    public static void main(String[] args) {

        int[] nums = { 1, 2, 3, 4, 5 };
        ListNode head = Tools.mnl(nums);
        // printNode(head);

        ListNode reHead = reverse(head);
        // printNode(reHead);

    }

    static ListNode reverse(ListNode head) {

        if (head == null || head.next == null) {
            return head;
        }
        print(head);
        ListNode lst = reverse(head.next);

        head.next.next = head;
        head.next = null;
        return lst;

    }

    static ListNode whileReverse(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    static void printNode(ListNode head) {

        if (head == null) {
            return;
        }
        System.out.println(head.val);
        printNode(head.next);

    }

    static void print(ListNode head) {
        System.out.println(head.val);
    }

}
