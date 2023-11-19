import java.util.Arrays;

public class MergeArray {

    public static void main(String[] args) {
        int nums1[] = { 1, 2, 3, 0, 0, 0 };
        int nums2[] = { 2, 4, 5 };

        new MergeArray().merge1(nums1, 3, nums2, 3);

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

    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int k = m + n;
        for (int i = n; i < k; i++) {

            nums1[i] = nums2[i - m];

        }

        printIntArray(nums1);
        Arrays.sort(nums1);
        printIntArray(nums1);

    }

    public void merge1(int[] nums1, int m, int[] nums2, int n) {
        int k = m + n;
        int[] newArray = new int[k];
        for (int i = 0, index1 = 0, index2 = 0; i < k; i++) {
            if (index1 >= m) {
                newArray[i] = nums2[index2++];
            } else if (index2 >= n) {

                newArray[i] = nums1[index1++];
            } else if (nums1[index1] < nums2[index2]) {
                newArray[i] = nums1[index1++];
            } else {
                newArray[i] = nums2[index2++];
            }
        }
        printIntArray(newArray);

    }

    // 1.study code write understanding
    // 2. moveZero

    // next, we will talk logic for today's class,

    // after we will do NodeList

}
