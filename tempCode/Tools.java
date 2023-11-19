import java.util.ArrayList;
import java.util.List;

public class Tools {

    public void printArray(int[] array) {
        List<Integer> list = new ArrayList<>();
        for (int i : array) {
            list.add(i);
        }
        System.out.println(list);

    }

    static void printListNode(ListNode n) {
        System.out.print("[");
        while (n.next != null) {
            System.out.print(n.val + ",");
            n = n.next;
        }
        System.out.print(n.val + "]");

    }

    // 创造一个节点
    static ListNode mn(int v) {
        return new ListNode(v);

    }

    /*
     * 创造一个数组包含了所有节点
     * 
     * 传入一个数字数组
     * 返回一个节点数组
     */
    static ListNode[] mna(int[] nums) {

        // 获取nums 多长
        int l = nums.length;
        /*
         * 根据 nums 里的每个数字，创造出对应的Node
         * 在把这个Node放到一个Array里返回
         */

        ListNode[] result = new ListNode[l];

        for (int i = 0; i < l; i++) {

            ListNode n = mn(nums[i]);

            result[i] = n;
        }

        return result;
    }

    /*
     * 传入一个节点数组 ， 一个循环位置，将节点数组变成循环的数组,
     * 数组的最后一位指向数组的 pos位置
     * 返回循环数组的头节点
     */

    static ListNode mcL(ListNode[] nodeArray, int pos) {
        int l = nodeArray.length;

        for (int i = 0; i < l - 1; i++) {

            int nextIndex = i + 1;

            nodeArray[i].next = nodeArray[nextIndex];

        }

        nodeArray[l - 1].next = nodeArray[pos];

        return nodeArray[0];

    }

    static ListNode mnl(int[] nums) {
        // 获取nums 多长
        int len = nums.length;
        /*
         * 根据 nums 里的每个数字，创造出对应的Node
         * 在把这个Node放到一个Array里返回
         */

        ListNode[] result = new ListNode[len];

        for (int i = 0; i < len; i++) {

            ListNode n = mn(nums[i]);

            result[i] = n;
        }

        for (int i = 0; i < len; i++) {
            if (i == len - 1) {
                result[i].next = null;
                break;
            }

            int nextIndex = i + 1;

            result[i].next = result[nextIndex];

        }

        return result[0];
    }

}
