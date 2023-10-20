import java.util.*;
public class JavaDic{
    public static void main(String args[]){
        System.out.println("Hello");
        //AA -> AB
        //AB -> BB
        //B -> AA

        //{'AA':'AB','AB':'BB','B':'AA'}    }
        Map<String, String> map = new HashMap<String, String>();
        map.put("AA","AB");
        map.put("AB","BB");
        map.put("B","AA");
        map.put("AA","AC");
        System.out.println(map.get("AA"));
        //MAP'S KEY IS UNIQUE
    }

    /*
     * pick 1 OR 2 for hw to do 
     * 
     * 1. repeated screen thread
     * 
     * 2. generic tree(CCC J5)
     * 
     *  ArrayList/Linked
     */


}