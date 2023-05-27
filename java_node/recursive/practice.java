public class practice {
    public static void main(String[] args) {
        int a=addrecursive(5);
        System.out.println(a);
        int b=peaches();
        System.out.println(b);
        int c=f(1);
        System.out.println(c);
        int d=f1(10);
        System.out.println(d);
    }
        
    public static int addrecursive(int n){
        if(n<=1){
            return 1;
        }else{
            return addrecursive(n-1)+n;
        }
    }
    /*
     * The monkey picked a bunch of peaches, 
     * ate half immediately, and then ate one more, 
     * and the next day, he ate the remaining half and one more...
        *There is only one peach left on the tenth day, how many peaches are there in total?
     */
    public static int peaches(){
        int peach = 1;
        for(int i = 0; i < 9; i++){
            peach = (peach + 1) * 2;
        }
        return peach;
    }

    public static int f(int day) {
        if(day == 10){
            return 1;
        }else{
            return (f(day+1) +1)  * 2;
        }

    }

    public static int f1(int day) {
        if(day == 1){
            return 1;
        }else{
            return (f1(day-1) +1)  * 2;
        }

    }

    

}
/*
 * draw image for fibnacci sequence
 */


/*
 * 1534
 */
