
import java.util.HashSet;
import java.util.Set;
import java.util.Iterator;
import java.util.TreeSet;

public class SetDemo {
    
    public static void main(String[] args) {
        createHashSet();
        System.out.println("");
        createTreeSet();
    }

    static void createHashSet(){
        /*
         * feature: (it is more faster than treeset, but it is unorder)
         * 1.   element is unique, 
         * 2.   * it is unorder, 
         * 3.   it can contain empty element
         * 4.   it does not have index
         * javac SetDemo.java
         * java SetDemo
         */
        Set<String> str = new HashSet<String>();
        
        str.add("second");
        str.add("third");
        str.add("first");
        
        // for(String i: str){
        //     System.out.println(i);
        // }

        // it is more fater
        Iterator<String> in = str.iterator();
        System.out.println("HashSet output");
        while(in.hasNext()){
            System.out.println(in.next());
        }


    }

    static void createTreeSet(){
        /*
         * feature: (it is inorder, but it is slower than hashset)
         * 1.   element is unique, 
         * 2.   *it is inorder, 
         * 3.   it can contain empty element
         * 4.   it does not have index
         * javac SetDemo.java
         * java SetDemo
         */
        Set<String> str = new TreeSet<String>();
        str.add("first");
        str.add("second");
        str.add("third");
        
        // for(String i: str){
        //     System.out.println(i);
        // }

        // it is more fater
        Iterator<String> in = str.iterator();
        System.out.println("TreeSet output");
        while(in.hasNext()){
            System.out.println(in.next());
        }


    }
}
