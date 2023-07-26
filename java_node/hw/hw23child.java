// you don't want to repeat yourself
public class hw23child<T> extends hw23father{
    
    public static void main(String[] args) {
        hw23child<String> john = new hw23child<>();
        john.setName("John");
        john.setAge(13);
        john.print(john.getName());
        john.print(john.getAge());

        hw23father johnFather = new hw23father();
        johnFather.setName("ABC");
        johnFather.setAge(35);
        johnFather.print(johnFather.getName());
    }
}

class hw23father{
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
    public <T> void print(T t){
        System.out.println(t);
    }


}

//one file three classes
// write all class in one file.
// write Animal class, Dog class, Cat class
// Dog extends Animal, Cat extends Animal
// you can try generic or nor generic
// extends to save code
/* 
public class Zoom{

}

class Animal{

}
class Dog extends Animal{

}
class Cat extends Animal{

}
*/