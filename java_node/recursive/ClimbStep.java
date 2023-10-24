import java.util.LinkedHashMap;

public class ClimbStep {
    /*
     * 
     * you want to climb step, purpose each time you only have 2 choice, each time ,
     * you can climb 1 step or 2 step, if you want to climb to 8 step, how many
     * choice
     * you will have?
     * 
     * //each time you can climb one or two step , if you want to climb 8 step, how
     * many choice you have
     * 
     * //1.build normal recursive, 2.make a advanced recursive, 3.consider to make a
     * while loop solution
     * 
     * //3 thinking how we can make a algorithem, make out code more faster.
     */
    public static void main(String[] args) {
        // find rule of sequence
        // 1,2,3,5,8 ....

        // 0 1 2 3 4

        int choice = recursiveClimb(8);
        System.out.println(choice);
    }

    static int recursiveClimb(int num) {
        if (num == 0)
            return 1;
        if (num == 1)
            return 2;
        else
            return recursiveClimb(num - 2) + recursiveClimb(num - 1);
    }

    public LinkedHashMap<Integer, Integer> library = new LinkedHashMap<>();

    public int advancedClimb(int num) {
        if (num == 0)
            return 1;
        if (num == 1)
            return 2;
        else {
            if (library.get(num) != null) {
                return library.get(num);
            } else {
                int result = advancedClimb(num - 2) + advancedClimb(num - 1);
                library.put(num, result);
                return result;
            }
        }
    }

}