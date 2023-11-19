public class MoveZeros {

    public static void main(String[] args) {
        int[] nums = { 0, 1, 0, 3, 12 };
        MoveZeros(nums);
        Tools.printIntArray(nums);
    }

    static void MoveZeros(int[] nums) {
        int j = 0;

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] != 0) {
                nums[j++] = nums[i];

            }
        }

        for (int i = j; i < nums.length; i++) {
            nums[i] = 0;
        }
    }

}
