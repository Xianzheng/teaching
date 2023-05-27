package practice2;

import javax.xml.validation.ValidatorHandler;

public class Practice3 {
    
    public static void main(String[] args) {
        int[] array={1,2,3,4};

        System.out.println("before swap");
        printArray(array);

        arraySwap(array);
        System.out.println("after swap");
        printArray(array);

    }

    static int[] swap(int a, int b){
        // int a = 1;
        // int b = 2;

        int temp = 0;

        temp = a;
        a = b;
        b = temp;
        int[] result = new int[2];
        result[0] = a;
        result[1] = b;
        return result;
        // System.out.println(a);
        // System.out.println(b);

    }

    static void arraySwap(int array[]){
        //{1,2,3,4}
        int temp = 0;
        temp = array[1];
        array[1] = array[3];
        array[3] = temp;
        
    }

    static void printArray(int array[]){
        for(int i: array){
            System.out.println(i);
        }
    }

    //{1,3,2,5,4,0} -> {0,1,2,3,4,5} do some algorithem
}
