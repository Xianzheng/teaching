
import java.util.*;

class FindDisappearNumber {
    public static void main(String[] args) {

        int[] nums = { 4, 3, 2, 7, 8, 2, 3, 1 };
        FindDisappearNumber solution = new FindDisappearNumber();
        System.out.println(solution.findDisappearedNumbers(nums));

    }

    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;

        for (int i : nums) {
            // System.out.println(i);
            if (i < 0)
                i = 0 - i;

            System.out.println(i - 1);
            if (nums[i - 1] > 0)
                nums[i - 1] = 0 - nums[i - 1];

        }

        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                result.add(i + 1);
            }
        }
        return result;
    }

}