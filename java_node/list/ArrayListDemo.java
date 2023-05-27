package list;
import java.util.ArrayList;
import java.util.Collections;

public class ArrayListDemo {
    public static void main(String[] args) {
        // createArray();
        creteArrayList();
    }

    static void createArray(){
        String[] sites = new String[3];
        sites[0] = "Google";
        sites[0] = "Facebook";
        sites[0] = "Twitter";
        System.out.println(sites);
    }

    static void creteArrayList(){
        //CRUD
        //Books book = new Books()
        //ArrayList<Books> bookLib = new ArrayList<Book>();
        //bookLib.add(book)
        ArrayList<String> sites = new ArrayList<String>();

        sites.add("Google");
        sites.add("Facebook");
        sites.add("Twitter");
        sites.add("Gmail");
        sites.add("Amazon");
        sites.add("Alibaba");
        System.out.println(sites);
        //do update
        sites.set(1,"QQ");
        System.out.println(sites);
    
        //do remove
        sites.remove(3);
        System.out.println(sites);

        //get size of ArrayList
        int size = sites.size();
        System.out.println(size);

        // for(String i : sites){
        //     System.out.println(i);
        // }

        for(int i = 0; i < size; i++){
           String element = sites.get(i);
           System.out.println(element);
        }

        System.out.println();
        Collections.sort(sites);

        for(int i = 0; i < size; i++){
            String element = sites.get(i);
            System.out.println(element);
         }

        //sites.
        


    }
}