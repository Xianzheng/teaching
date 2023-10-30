import java.util.HashMap;

class ClimbStep{
    public static void main(String args[]){

        int choice = new ClimbStep().forWay(11);
        System.out.println(choice);

    }

    static int recursiveWay1(int step){
        if (step == 1 ){
            return 1;
        }else if(step ==2){
            return 2;
        }else {
            return recursiveWay1(step - 2 ) + recursiveWay1(step - 1 ); 

        }

    }
     private HashMap<Integer, Integer> map = new HashMap<>();
    public int recursiveWay2(int step){

        if (step == 1 )return 1;

        if(step == 2)    return 2;

        if (map.get(step) != null){
            return map.get(step);
        }else{
            int result =  recursiveWay1(step - 2 ) + recursiveWay1(step - 1 ); 
            map.put(step,result);
            return result;
        }
            

    }

    public int forWay(int step){
        if (step == 1 ){
            return 1;
        } else if (step == 2){
            return 2;
        } else{
            int pre = 2;
            int prepre = 1;
            int result = 0;

            for(int i = 3; i <= step; i++){
                result = pre + prepre;
                prepre = pre;
                pre = result;
            }

            return result;
        }



    }


    


}