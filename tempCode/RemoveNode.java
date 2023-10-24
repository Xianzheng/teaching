public class RemoveNode {
    public static void main(String[] args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(1);
        list1.next.next = new ListNode(2);
        list1.next.next.next = new ListNode(2);

        ListNode l3 = solution(list1);

        printList(l3);

    }

    static ListNode solution(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode p = head;

        while (p.next != null) {
            if (p.val == p.next.val) {
                p.next = p.next.next;
            } else {
                p = p.next;
            }
        }

        return head;

    }

    static ListNode reMergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null)
            return list2;
        if (list2 == null)
            return list1;
        else {
            if (list1.val < list2.val) {

                list1.next = reMergeTwoLists(list1.next, list2);
                return list1;

            } else {
                list2.next = reMergeTwoLists(list1, list2.next);
                return list2;
            }
        }
    }

    static void printList(ListNode n) {
        System.out.print("[");
        while (n.next != null) {
            System.out.print(n.val + ",");
            n = n.next;
        }
        System.out.print(n.val + "]");

    }

}
