import java.util.*;
class MoveZeros {

    // 283 99%
    public static void main(String[] args) {
        int[] nums = {0,1,0,3,12};
        new MoveZeros().moveZeroes(nums);
        printArray(nums);

    }

    public void moveZeroes(int[] nums) {

        int j = 0;

        for(int i = 0; i < nums.length; i ++){
            if (nums[i] !=0){
                nums[j ++] = nums[i];
            }
        }

        for (int i = j; i< nums.length; i ++){
            nums[i] = 0;
        }
        
    }

    static void printArray(int[] array){
        List<Integer> list=new ArrayList<>();
        for(int i:array){
            list.add(i);
        }
        System.out.println(list);

    }

}