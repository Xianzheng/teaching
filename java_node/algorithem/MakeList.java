public class MakeList {
    public static void main(String[] args) {
        // ListNode node1=Tools.mn(1);
        // ListNode node2=Tools.mn(1);
        // ListNode node3=Tools.mn(1);
        // ListNode node4=Tools.mn(1);

        // node1.next=node2;
        // node2.next=node3;
        // node3.next=node4;

        // Tools.printListNode(node1);

        // int[] nums = { 1, 2, 3, 4, 5 };
        // ListNode h1 = new MakeList().min(nums);
        // Tools.printListNode(h1);

        // int[] nums = { 1, 2, 3, 4, 5 };

        // ListNode h1 = new MakeList().mln(nums);
        // Tools.printListNode(h1);

        int[] nums1 = { 1, 2, 3, 4 };
        ListNode head = new MakeList().mln(nums1);

        // deleteNode(head, 2);
        // deleteNode(head, 4);

        addNodeToListNode(head, 7, 2);
        addNodeToListNode(head, 7, 2);
        addNodeToListNode(head, 7, 4);
        retrieveListNode(head);

    }

    ListNode min(int[] nums) {
        int len = nums.length;
        Tools.printIntArray(nums);

        ListNode[] result = new ListNode[len];

        for (int i = 0; i < len; i++) {
            ListNode n = new ListNode(nums[i]);
            n.pos = i;
            result[i] = n;
        }

        for (int i = 0; i < len; i++) {
            if (i == len - 1) {
                break;
            }

            int nextIndex = i + 1;

            result[i].next = result[nextIndex];
        }

        return result[0];// return the array as a list node
    }

    ListNode mln(int[] nums) {
        int len = nums.length;

        ListNode[] result = new ListNode[len];

        for (int i = 0; i < len; i++) {
            ListNode n = new ListNode(nums[i]);
            n.pos = i;
            result[i] = n;
        }

        for (int i = 0; i < len; i++) {

            if (i == len - 1) {
                break;
            }

            int nextIndex = i + 1;

            result[i].next = result[nextIndex];
        }

        return result[0];
    }

    static void retrieveListNode(ListNode head) {

        while (head != null) {

            System.out.println(head.val + " and pos is " + head.pos);
            head = head.next;

        }

    }

    static void deleteNode(ListNode head, int val) {

        while (head.next != null) {

            if (head.next.val == val) {
                head.next = head.next.next;
            } else {
                // System.out.println(head.val);

                head = head.next;
            }

        }

    }

    static void deleteNodeRecursive(int val, ListNode head) {

        if (head.next != null) {
            if (head.next.val == val) {
                head.next = head.next.next;
            } else {
                System.out.println(head.val);

                head = head.next;
            }
            deleteNodeRecursive(val, head);
        }

    }

    // add a node val 7 in second position of this list
    // 1 - 2 - 3 - 4
    static void addNodeToListNode(ListNode head, int val, int pos) {

        ListNode curr = head;

        while (curr != null) {
            // System.out.println(curr.val);

            if (curr.next.pos == pos) {
                break;
            }

            curr = curr.next;
        }

        ListNode newNode = new ListNode(7);
        newNode.next = curr.next;
        curr.next = newNode;

        // to trim again
        ListNode otherPointer = head;

        int index = 0;
        while (otherPointer != null) {
            otherPointer.pos = index;
            index += 1;
            otherPointer = otherPointer.next;
        }

    }
    /*
     * static void addNodeToListNode(ListNode head,int val,int pos,int temppos){
     * //homework for monday:
     * //add value 7 in second position of this list
     * 
     * if(head.next!=null){
     * if(temppos==pos-1){
     * head.next.next=head.next;
     * head.next=new ListNode(7);
     * temppos+=1;
     * }else{
     * System.out.println(head.val);
     * 
     * head=head.next;
     * temppos+=1;
     * }
     * addNodeToListNode(head, val,pos,temppos);
     * }
     */
}
