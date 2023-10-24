
public class MergeList {
    public static void main(String[] args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(4);

        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(5);

        ListNode l3 = reMergeTwoLists(list1, list2);

        printList(l3);

    }

    static ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if (list1 == null)
            return list2;

        if (list2 == null)
            return list1;

        ListNode result = new ListNode(0);

        ListNode p = result;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                p.next = list1;
                list1 = list1.next;
            } else {
                p.next = list2;
                list2 = list2.next;
            }
            p = p.next;
        }

        if (list1 == null)
            p.next = list2;

        if (list2 == null)
            p.next = list1;

        return result.next;
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
