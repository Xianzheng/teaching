package array;

public class ArrayDemo {
    public static void main(String []args){
        // practice_intArray();
        // practice_stringArray();
        // when we want to create a whatever a type array
        // datatype[] variableName = new datatype[length];
        //initially assign element to array
        int[] numberArray = {1,2,3,4,5,6};

        for(int i: numberArray){
            System.out.println(i);
        }
    }

    static void practice_stringArray(){
        String[] stringArray = new String[3];

        stringArray[0] = "apple";
        stringArray[1] = "banana";
        stringArray[2] = "cherry";

        for(String i: stringArray){
            System.out.println(i);
        }
    }

    static void practice_intArray(){
        int[] intArray = new int[3];

        intArray[0] = 1;
        intArray[1] = 2;
        intArray[2] = 3;
        intArray[1] = 4;
        //intArray[3] = 10; it will give a error, since this array
        //only allows 3 element;

        //System.out.print it will print one by one
        //System.out.println it will print next line
        // System.out.println(intArray[0]);
        // System.out.println(intArray[1]);
        // System.out.println(intArray[2]);
        for(int i: intArray){
            System.out.println(i);
        }

        for(int i = 0; i<intArray.length; i++){
            System.out.println(intArray[i]);
        }

    }
}
