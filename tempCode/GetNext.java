import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

public class GetNext {
    public static HashMap<String, String> dic = new HashMap<String, String>() {{
        put("AA", "AB");
        put("AB", "BB");
        put("B", "AA");
    }};
    
    public static List<String> nextLevel(String str) {
        List<String> lst = new ArrayList<String>();
        for (int i = 0; i < str.length(); i++) {
            for (int j = 0; j <= max; j++) {
                if (i + j <= str.length()) {
                    String result = change(str, str.substring(i, i + j), i, i + j);
                    if (result != null) {
                        lst.add(result);
                    }
                }
            }
        }
        return lst;
    }
    
    public static String change(String str, String str1, int s, int t) {
        if (dic.containsKey(str1)) {
            return makeChange(str, dic.get(str1), s, t);
        }
        return null;
    }
    
    public static String makeChange(String str, String str1, int s, int t) {
        // System.out.println("s="+s);
        // System.out.println("t="+t);
        // System.out.println("str"+str);
        // System.out.println("str1"+str1);
        // char[] lst = str.toCharArray();

        // for (int i = s; i < t; i++) {
        //     lst[i] = str1.charAt(i - s);
        // }
        // return new String(lst);
        // return str.replace()
        StringBuilder sb = new StringBuilder(str);
        sb.replace(s,t,str1);
        return sb.toString();
    }
    
    public static int max = 0;
    
    public static void main(String[] args) {
        for (String i : dic.keySet()) {
            if (max < i.length()) {
                max = i.length();
            }
        }
        String start = "BB";
        System.out.println(nextLevel(start));
    }
}