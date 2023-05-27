public class Recursive {
    public static void main(String[] args) {
        // for(int i = 1; i < 5; i++){
        //     System.out.println(i);
        // }
        // recursiveDemo1(5);
        // int a =  factorial(3);
        // System.out.println(a);

        // int b = f(5);
        // System.out.println(b);

        int c = fib(7);
        System.out.println(c);

    }

    public static void recursiveDemo1(int n){
        if (n > 1){
            recursiveDemo1(n - 1);
        }
        System.out.println(n);
    }

    public static int factorial(int n){
        int result = 1;
        for(int i = n; i > 0; i--){
            result *= i;
            // System.out.println(i);
        }

        return result;

    }
    public static int f(int n){
        if (n == 1){
            return 1;
        } else {
            return n * f(n - 1);
        }
    }

    public static int fib(int n){
        if (n == 1){
            return 1;
        }else if (n == 2){
            return 1;
        }else{
            return fib(n - 2) + fib(n - 1);
        }
    }
    
}
/*
 * Topic: The monkey picked a few peaches on the first day, 
 * and ate half of them immediately.
 *  He still didn’t satisfy his hunger, so he ate another one; 
 * Every day I eat half of the remaining one from the previous day, 
 * and when I want to eat again on the 10th day, there is only one peach left. 
 * Ask how many peaches were picked on the first day?
 */
