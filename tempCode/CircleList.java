public class CircleList {

    public static void main(String[] args) {
        int[] nums = { 3, 2, 0, -1 };
        ListNode head = mCLN(nums, 1);
        Tools.printListNode(head);

    }

    /*
     * 通过传入一个数组，和指定循环的位置，创造一个环形节点数组并返回节点头
     * 
     * 方法 mna： 创造一个数组包含了所有节点
     * 
     * 方法 mcL: 把所有节点变成一个链表
     * 
     * 最终把链表变成一个环形链表，在返回头节点
     * 
     * 最终
     */
    static ListNode mCLN(int[] nums, int pos) {

        ListNode[] nodeArray = Tools.mna(nums);

        ListNode circleHead = Tools.mcL(nodeArray, pos);

        return circleHead;
    }

}
