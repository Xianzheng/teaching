
// package practice2;
// import java.util.Scanner;

// public class Practice2 {
//     public static void main(String[] args) {
//         test();
//     }
//     static void test(){
//         // Scanner scan = new Scanner(System.in);
//         // System.out.println("Please type something");
//         // String a = scan.nextLine();

//         String comp = "12 +";
//         parsing(comp);
//         System.out.println();

    
//     }

//     static void parsing(String s){
//         String array[] = s.split(" ");

//         int times = Integer.parseInt(array[0]);

//         String character = array[1];

//         for(int i=0;i<times;i++){
//             System.out.print(character);
//         }

//     }
// }

package practice2;

import java.util.Scanner;

public class Practice2 {
    public static void main(String[] args){
        // test();
        test1();
    }

    static void test1(){
        System.out.println(3 % 2);
    }
    static void test(){
        //how to input:
        // Scanner scan=new Scanner(System.in);
        // System.out.println("Please type something");
        // String a=scan.nextLine();
        //String a="a b c d";
        
        // System.out.println(a.split(" "));

        //String f[]=a.split(" ");
        Scanner scan=new Scanner(System.in);
        int num=scan.nextInt();
        
        String letters[]= new String[num];
        int amount[]=new int[num];
        for (int i=0; i<num;i++){
            Scanner scan1=new Scanner(System.in);
            String inp=scan1.nextLine();
            
            String split[]=inp.split(" ");
            String first=split[1];
            int second=Integer.parseInt(split[0]);
            letters[i]=first;
            amount[i]=second;
           
        }
        for (int i=0;i<num;i++){
            String print="";
            for (int e=0;e<amount[i];e++){
                print+=letters[i];
            }
            System.out.println(print);
        }

        // for (String e:f){
        //     System.out.println(e);
        // }
        // String c="4";
        // int v=Integer.parseInt(c);
        // System.out.println(v);
        
        
        
    }
}
