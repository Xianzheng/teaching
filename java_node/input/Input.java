package input;
import java.util.Scanner;

public class Input {
    public static void main(String []args){

        // practice();
        practice1();
    }

    static void practice(){
        System.out.println("ok");
        // make a instance of Scanner
        Scanner scan = new Scanner(System.in);
        int a1 = scan.nextInt();
        Scanner scan1 = new Scanner(System.in);
        int a2 = scan1.nextInt();
        Scanner scan2 = new Scanner(System.in);
        int a3 = scan2.nextInt();
        Scanner scan3 = new Scanner(System.in);
        int b1 = scan3.nextInt();
        Scanner scan4 = new Scanner(System.in);
        int b2 = scan4.nextInt();
        Scanner scan5 = new Scanner(System.in);
        int b3 = scan5.nextInt();

        int apple = a1 * 3 + 2 * a2 + a3 ;
        int banana = b1 *3 + 2 * b2 + b3;


        System.out.println(apple);
        System.out.println(banana);

        if (apple > banana){
            System.out.println("A");
        }
        if (apple < banana){
            System.out.println("B");
        }
        if (apple == banana){
            System.out.println("T");
        }

    }

    static void practice1(){
        Scanner scan1 = new Scanner(System.in);
        String str1 = scan1.nextLine();
        Scanner scan2 = new Scanner(System.in);
        String str2 = scan2.nextLine();

        System.out.println(str1);
        System.out.println(str2);
    }
}
