package gui;

public class GenericDemo extends Animal{
    
    public static void main(String[] args) {
        GenericDemo demo = new GenericDemo();
        demo.setName("abc");
        //print(demo.getName())
        print(demo.getName());
        //print(demo.getAge())
        demo.setAge(10);
        print(demo.getAge());
    }
    
}

class Animal {


    // attributes
    private String name = null;

    private int age = 0;

    public void setName(String name){
        this.name = name;
    }

    public void setAge(int age){
        this.age = age;
    }

    public String getName(){
        return this.name;
    }

    public int getAge(){
        return this.age;
    }

    public static <T> void print(T t){
        System.out.println(t);
    }

}
