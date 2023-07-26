package generic;
import java.util.*;
public class genericDemo {
    public static void main(String[] args) {
        /* 
        System.out.println("works");
        List<String> v = new ArrayList<String>();// List is a interface, ArrayList implements List
        v.add("test1");
        v.add("test2");
        v.add("test3");
        System.out.println(v);

        List<Integer> v1 =  new ArrayList<Integer>();
        v1.add(0);
        v1.add(1);
        v1.add(2);
        System.out.println(v1);
        
        Integer[] i1 = {1,2,3,4,5};
        Double[] d1 = {1.1,2.2,3.3,4.4};
        Character[] c1 = {'A','B','C'};
        printArray(d1);

        Something<Integer> s1 = new Something<Integer>();
        s1.setInto(1);
        System.out.println(s1.getinfo());
        
        Something<String> s2 = new Something<String>();
        s2.setInto("Mark");
        System.out.println(s2.getinfo());
        */
        //Integer represent food
        Something<Integer> s1 = new Something<Integer>();
        s1.setInto(1);

        //Double represent book
        Something<Double> s2 = new Something<Double>();
        s2.setInto(1.1);

        //String represent person
        Something<String> s3 = new Something<String>();
        s3.setInto("Mark");

        List<Something> l1 = new ArrayList <Something>();

        l1.add(s1);
        l1.add(s2);
        l1.add(s2);
        System.out.println(l1);

        System.out.println(l1.get(0).getinfo());

        


    }
    //T（tyle）E（element）K(key) V(value)
    public static <E> void printArray(E[] inputArray)
    {
        for( E element: inputArray){
            System.out.println(element);
        }
    }


}

class Something<T>{
    private T info;

    public T getinfo(){
        return info;
    }

    public void setInto(T info){
        this.info = info;
    }

}

/*
 * try to create a arraylist that store different type, for example store int, double, string
 * 
 * int using generic
 * 
 *  */





