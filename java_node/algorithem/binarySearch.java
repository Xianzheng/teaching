package algorithem;

public class binarySearch {
    public static void main(String[] args) {
        int[] array = new int[10000];
        for(int i =0; i<10000;i++){
            array[i] = i +  1;
           
        }

        System.out.println(runbBinarySearch(array,0,9999,7500));
        
    }

    //recursive + binary search  

    static int runbBinarySearch(int[] arr,int start, int end,int hkey){

        if (start > end)
            return -1;

        int mid = start + (end - start)/2;  

        if (arr[mid] > hkey)
        return runbBinarySearch(arr, start, mid - 1, hkey);

        if(arr[mid] < hkey){
        return runbBinarySearch(arr,mid + 1,end,hkey);
        }

        return mid;
    }

    
}
