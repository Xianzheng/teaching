// public private default proteced

public class Tools {
    public static void main(String[] args) {

    }

    static void printIntArray(int[] nums) {
        System.out.print("[");
        for (int i = 0; i < nums.length; i++) {

            System.out.print(nums[i]);

            if (i != nums.length - 1) {
                System.out.print(",");
            }

        }
        System.out.print("]");
    }

    static ListNode mn(int val) {
        return new ListNode(val);
    }

    public static void printListNode(ListNode head) {
        System.out.println(head.val);
        if (head.next == null) {
            return;
        }

        printListNode(head.next);
        ;
    }

}
/**
 * public static void printListNode(ListNode head){
 * System.out.println(head.val);
 * if(head.next==null){
 * return;
 * }
 * 
 * printListNode(head.next);;
 * }
 */