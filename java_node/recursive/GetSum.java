public class GetSum {

    public static void main(String[] args) {
        // calculate the sum of 1 to 100
        whileWay();
        loopWay();
        mathWay();
        int[] nums = { 3, 4, 5, 7, 9, 6 };
        // 0 1 2 3 4 5
        int target = 10;
        int result[] = getSum(nums, target);
        // result should be {0,3}

        int target1 = 11;
        int result1[] = getSum(nums, target1);
        // result1 should be {1,3}

    }

    // previous hw: climb question, consider to make a while loop solution

    // finish getSum
    // 1. make a solution of question(requirement)
    // 2. make new Algorithm to make it faster(*)

    static int[] getSum(int[] nums, int target) {

        int result[] = new int[2];

        return result;
    }

    static void whileWay() {
        // second fast
        // 0(logN)
        int i = 0;
        int sum = 0;
        while (i < 100) {
            i += 1;
            sum += i;
        }
        System.out.println(sum);
    }

    static void loopWay() {
        // last fast
        // O(N)
        int sum = 0;
        for (int i = 0; i <= 100; i++) {
            sum += i;
        }
        System.out.println(sum);
    }

    static void mathWay() {
        // MOST FAST
        // o(1)
        System.out.println((1 + 100) * 50);
    }

    // algorithem : 1. make a solution of question, 2. we need to make it faster

}

// Get Sum , consider we have have array , {3,4,5,7,9,6}
