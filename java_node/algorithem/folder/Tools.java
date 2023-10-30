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
}
