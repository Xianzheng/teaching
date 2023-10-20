import java.util.HashMap;

class TwoNumberSum {
    public static void main(String args[]){

        int[] array = {2,7,11,15};
        int target = 9;

        int[] result = new TwoNumberSum().solution(array,target);
        for (int i: result){
            System.out.println(i);
        }
        //可以用暴破做
    }

    public int[] solution(int[] array, int target){
        int[] result = new int[2];
        HashMap<Integer,Integer> map = new HashMap<>(); //<value:index>
        for (int i = 0;i < array.length; i ++){
            
            int value = target - array[i];

            if (map.get(value) != null){
                result[0] = map.get(value);
                result[1] = i;
                break;
            }else{
                map.put(array[i],i);
            }
            System.out.println(map);
        }

         
        return result;
    }
}