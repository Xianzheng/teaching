import java.util.ArrayList;
import java.util.List;
//leed code 88
public class mergeArray {

    public static void main(String args[]){
        int nums1[] = {1,2,3,0,0,0};
        int nums2[] = {2,4,5};
        new mergeArray().merge(nums1, 3, nums2, 3);
        printArray(nums1);
    }
    //nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

    //[1,2,2,3,5,6]
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int k = m + n;
        int[] newArray = new int[k];
        for (int i = 0, index1 = 0, index2 = 0; i < k; i++){
            if(index1 >= m){
                newArray[i] = nums2[index2 ++];
            }else if(index2 >= n){

                newArray[i] =  nums1[index1 ++];
            }else if(nums1[index1] < nums2[index2]){
                newArray[i] = nums1[index1 ++];
            }else{
                newArray[i] = nums2[index2 ++];
            }
        }
        for (int i = 0; i < newArray.length; i++){
            nums1[i] = newArray[i];
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
