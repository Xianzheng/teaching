
import java.util.HashMap;

public class GetSum {
    public static void main(String[] args) {

        int[] nums = { 3, 4, 5, 6, 8 };
        // if nums's length is 1000 then O(n^2) will let computer to calculate 10000
        // times
        int target = 10;

        // Tools.printIntArray(getSum(nums, target));
        Tools.printIntArray(advMethod(nums, target));

    }

    static int[] getSum(int[] nums, int target) {
        // return {0,3}
        // you return {0,3} since those are the index of 3 and 7 which when you add up
        // is 10
        // this function get back the numbers in the array that adds up to the target.
        int result[] = new int[2];

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                int temp = target - nums[i];
                if (temp < 0) {
                    temp = temp * -1;
                }

                if (temp == nums[j]) {

                    result[0] = i;
                    result[1] = j;
                    return result;

                }
            }
        }
        return result;
    }

    static int[] advMethod(int[] nums, int target) {

        int[] result = new int[2];

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int value = target - nums[i];

            // map.put(nums[i],i)
            if (map.get(value) != null) {
                result[0] = map.get(value);
                result[1] = i;
                break;
            } else {
                map.put(nums[i], i);
            }
        }
        return result;

    }

    // rewrite GetSum advance Method
    // adding your understanding for each line
    // I will put another algorithm question for thinking

}