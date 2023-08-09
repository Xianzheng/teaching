package CCC;
import java.util.Scanner;
public class CCC2020 {
    public static void main(String[] args){
        //rotate("abcde");
        // String str = "ABCDE";
        // char[] a = str.toCharArray();
        // show(a);

        String a = "ABCDEFGH";
        String b = "CDE";
        System.out.println(a.contains(b));

        String s = "ABCDE";
        StringBuilder builder = new StringBuilder(s);
        char tem = s.charAt(0);
        builder.deleteCharAt(0);
        builder.append(tem);
        System.out.println(builder.toString());




        

    }

    static void show(char[] a){
        for(char i: a){
            System.out.println(i);
        }
    }

    static void yourCode(){
        Scanner scan1 = new Scanner(System.in);
        String thestr=scan1.nextLine();
        Scanner scan2 = new Scanner(System.in);
        String str=scan2.nextLine();
        String cyclicshift=str;
        int check=0;

        for(int i=0;i<str.length();i++){
            if(thestr.contains(cyclicshift)){
                check++;
                break;
            }else{
                //System.out.println(cyclicshift);
                cyclicshift=rotate(cyclicshift);
                
            }
        }
        if(check>0){
            System.out.println("yes");
        }else{
            System.out.println("no");
        }
    }

    static String rotate(String str){
        String[] lst=str.split("");
        String newstr="";
        for(int i=0;i<lst.length;i++){
            
            if(lst[i]==lst[0]){
                continue;
            }else{
                newstr+=lst[i];
            }
        }
        newstr+=lst[0];
        
        return(newstr);
    }

    
}

/*
 * using stringBuilder to Code more simple
 * 
 * Try CCC 2016 j4 https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
 */
