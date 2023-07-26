package CCC;
public class CCC2019{
    public static void main(String[] args) {
        /* 
       String a = "+++===!!!!";
       System.out.println(a);
       System.out.println(a.charAt(0));
       char[] charArray = a.toCharArray();
       System.out.println(charArray[0]);
      
      //compare
      String a = "apple";
      String b = "apple";
      System.out.println(a == b);

      String c = new String("apple");
      System.out.println(c);
      String d = new String("apple");
      System.out.println(d);
      System.out.println(c.equals(d));
      

    //   char a = 'b';
    //   char b = 'b';
    //   System.out.println(a == b);
      String a = "+++===!!!!";
      char[] charArray = a.toCharArray();
      System.out.println(charArray);
      System.out.println(charArray[5]); //python
      System.out.println(charArray[0] == charArray[1]);
      */

      String a = "abcd"; //change a to abdd
      char[] aa = a.toCharArray();
      aa[2] = 'd';
      String d = aa.toString();
      a = d;
      System.out.println(a);





     


    }

}