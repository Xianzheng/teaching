

import java.util.*;

public class subString {
    //TOOO Auto-generate method stub
    /*
     * substring
     */
    /*
     * stringBuilder
     */
    /*
     * changeString
     */
    public static void main(String args[]){

    

    //get possible output for change string base on Hashmap dictionary?
    //["BBC","AAA"]
    List<String> list=new ArrayList<String>();

    // System.out.println(list);
    
    String test = "ABCDAB"; //["BBCDAB","AAADAB","ABDDAB","ABCDBB"]
    //             012345
    //temp.replace(i,i+j,dic.get(changeStr));
            //0  2
            //4  6
    // we need to get the max length of key of hashmap 
    int maxLengthOfKey = 0;
    
    for (String i: dic.keySet()){
        if (maxLengthOfKey < i.length()){
            maxLengthOfKey = i.length();
        }
    }
    // System.out.println(maxLengthOfKey);

    for (int i = 0; i < test.length();i++){
        for (int j = 0; j <= maxLengthOfKey; j ++){
            if ( i + j <= test.length()){
                String changeStr = test.substring(i, i + j);
                if (changeStr != ""){
                // System.out.println(changeStr);
                    if(dic.containsKey(changeStr)){
                        StringBuilder temp = new StringBuilder(test);
                        temp.replace(i,i+j,dic.get(changeStr));
                        // System.out.println(temp);
                        list.add(temp.toString());
                    }
                }
            }
        } 
    }

    
    System.out.println(list);

    
    // for (int i = 0; i < test)
            
    

}
    public static HashMap<String,String>dic=new HashMap<String,String>(){{
        put("AB","BB");
        put("BC","AA");
        put("C","D");
    }
    };
    static <E> void print(char[] e){
        for(char i : e){
            System.out.println(i);
        }
    }
}

