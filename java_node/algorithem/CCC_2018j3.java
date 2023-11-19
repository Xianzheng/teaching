
import java.util.Scanner;

public class CCC_2018j3 {
    public static void main(String[] args) {
        int[] init = makeInitArray();

        for (int i = 0; i < init.length; i++) {
            for (int j = 0; j < init.length; j++) {
                int temp = init[i] - init[j];
                if (temp < 0) {
                    temp = 0 - temp;
                }
                System.out.print(temp);
                System.out.print(" ");
            }
            System.out.println();

        }

    }

    static int[] makeInitArray() {

        Scanner scan1 = new Scanner(System.in);

        String inp = scan1.nextLine();

        String[] temparray = inp.split(" ");

        int[] resultArray = new int[temparray.length + 1];

        resultArray[0] = 0;

        int temp = 0;

        for (int i = 0; i < temparray.length; i++) {

            temp += Integer.parseInt(temparray[i]);

            resultArray[i + 1] = temp;
        }

        return resultArray;

    }

    static void printArray(int[] array) {
        for (int i : array) {
            System.out.println(i);
        }
    }
}
