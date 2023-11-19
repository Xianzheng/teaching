
public class BubbleSort {
    public static void main(String[] args) {
        int[] array = { 3, 2, 1, 5, 4 };
        makeSort(array);
        printArray(array);

    }

    // (i ++) ==( i += 1) == (i = i+ 1)
    static void makeSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] > array[j]) {
                    swap(array, i, j);
                    // printArray(array);
                }
            }
        }
    }

    static void swap(int[] array, int p1, int p2) {
        int temp = array[p1];
        array[p1] = array[p2];
        array[p2] = temp;
    }

    static void printArray(int[] array) {
        for (int i : array) {
            System.out.print(i);
            System.out.print(" ");
        }
        System.out.println();
    }

}
