package twoDimensionalArray;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
/*
 *  1 3  [[1,3],[2,9]]
 *  2 9   0 1   0  1
 *         
 *        [[2,1],[9,3]] [[9,2],[1,3]]
 * 
 * 
 * 4 3 1    
 * 6 5 2
 * 9 7 3
 */

public class twoDArray {
    
    public static void main(String[] args){
        
            // int [][] array = {{3,7,9},{2,5,6},{1,3,4}};
            
            // int [][] afterRotate = rightrotation(array);

            // boolean result = check(array);
            // System.out.print(result);

            /*
             * if/* array follows rule, we don't need to rotate
             * if it does not, we need to rotate, until it follows rule
             * and then print it.
             */

             int [][] array = j4();

             while(check(array) != true){
                array = rightrotation(array);
             }

             printArray(array); 
             
    }
    static int[][] j4(){
        Scanner scan= new Scanner(System.in);
        int inp=scan.nextInt();
        int[][] twodarray=new int[inp][inp];
        
        for (int i=0;i<inp;i++){
            
            Scanner scan1= new Scanner(System.in);
            String inp1=scan1.nextLine();
            String[] temparray=inp1.split(" ");
            for(int j=0;j<inp;j++){
                
                twodarray[i][j]=Integer.parseInt(temparray[j]);
            }
            
        }
        for(int h=0;h<twodarray.length;h++){
            for(int k=0;k<twodarray.length;k++){
                //System.out.println(twodarray[h][k]);
            }
        }
        return twodarray;
    }
    static int[][] leftrotation(int[][] array){
        int[][] temparray=new int[array.length][array.length];
        int count=0;
        for(int i=0;i<array.length;i++){
            for (int j=0;j<array.length;j++){
                temparray[i][j]=array[j][2-i];             
                
            }
        }
        
        return temparray;
    }
    static int[][] rightrotation(int[][] array){
        int[][] temparray=new int[array.length][array.length];
        int count=0;
        for(int i=0;i<array.length;i++){
            for (int j=0;j<array.length;j++){
                temparray[i][j]=array[array.length - 1-j][i];
                
            }
        }
        
        return temparray;
    }
    static boolean check(int[][] array){
        int num=0;
        
        for(int i=0;i<array.length;i++){
            int[] temparray=new int[array.length];
            int[] currentarray=new int[array.length];
            int[] newtemparray=new int[array.length];
            int[] testarray=new int[array.length];
            
            for (int j=0;j<array.length;j++){
                newtemparray[j]=array[j][i];
                testarray[j]=array[j][i];
                temparray[j]=array[i][j];
                currentarray[j]=array[i][j];
                
                
            }
            Arrays.sort(temparray);
            if (Arrays.equals(currentarray,temparray)){
                num++;
                
            }
            Arrays.sort(newtemparray);
            if (Arrays.equals(testarray,newtemparray)){
                num++;
                
            }
            // System.out.println(array[i]);
            
        }
        if (num== array.length * 2){
            return true;
        }else{
            return false;}
    }

    static void printArray(int [][] array){
        for (int[] a : array){
            for (int b: a){
                System.out.print(b+" ");
                
            }
            System.out.println();
        }
    }
}
//how to sort arrays: int[] array1={1,2,5,3,8,3} 
//arrays.sort(array1)
//1 3 
//2 9

//hw: try doing this https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf
//hw: must find rule of rotation and also rotate once a original input then print it out.

// 4 3 1
// 6 5 2
// 9 7 3

//new hw 2023/04/17: do second stage of problem. Hint: do array[0] and use sort to see if its good or not example: array[0]==sorted(array[0]);