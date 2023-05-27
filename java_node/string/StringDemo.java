package string;


public class StringDemo {

    public static void main(String args[]){
        stringDemo();
        
    }

    static void stringDemo(){
        /* 
        System.out.println("It works");
        // create string in direct way
        String str = "this is a string";
        //            01234567....
        System.out.println(str);

        //invoke String class to create a string
        String str1 = new String("this is a another string");
        System.out.println(str1);

        System.out.println(str.charAt(3));

        System.out.println(str.length());
        
        
        for(int i = 0; i < str.length(); i++){

            System.out.print(str.charAt(i));

        }
        System.out.println("");

        int i = 0;
        while (i < str.length()){
            System.out.print(str.charAt(i));
            i += 1;
        }
        */

        String a = new String("1");
        String b = new String("1");
        System.out.println(a);
        System.out.println(b);
        System.out.println(a == b);// compare reference, address
        if (a.equals(b)){//compare two objects' value
            System.out.println("equals");
        }

    }

   


}
/*
 * make two strings (same content, different content)
 * loop all content of string(while , loop)
 * compare the address and content
 */
