import java.util.HashMap;

public class AdvFib {

    //1 1 2 3 5 8 13 21 ....
    //1 2 3 4 5 6
    public static void main(String[] args) {
        
        int result1 = new AdvFib().f(6);
        int result2 = new AdvFib().advF(6);
        int result3 = new AdvFib().whileF(6);
        System.out.println(result3);

        
    }

    public HashMap<Integer, Integer> map = new HashMap<>();

    public int f(int i){
        if (i == 1) return 1;
        if (i == 2) return 1;
        else{
            return f(i - 2) + f(i - 1);
        }

    }

    public int advF(int i){
        if (i == 1) return 1;
        if (i == 2) return 1;
        else {
            if (map.get(i) != null){// for node 
                return map.get(i);
            }else{
                int result = f(i - 2) + f(i - 1);
                map.put(i, result);
                return result;
            }
        }
    }

    public int whileF(int i){
        int a = 1;
        int b = 1;
        int result = 0;

        for(int j = 1; j < i - 1; j++){
            result = a + b;
            a = b;
            b = result;

        }

        return result;


    }

    /*
     * When n=1, just climbing one step is a solution.
        When n=2, you can walk one floor twice or walk two floors once.
        When n=3, you may be on the first or second floor. When you are on the first floor, 
        it is equivalent to you being on the 0th floor preparing to go to the second floor. When you are on the second floor, it is equivalent to you being on the 2nd floor. Level 0 is ready to go to Level 1.
        And so on.
     */

     //each time you can climb one or two step , if you want to climb 8 step, how many choice you have(dynamic option) (8, 0)

     //1.build normal recursive, 2.make a advanced recursive, 3.consider to make a while loop solution

     //3 thinking how we can make a algorithem, make out code more faster.


}
