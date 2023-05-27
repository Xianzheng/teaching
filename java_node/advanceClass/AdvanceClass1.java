package advanceClass;

public class AdvanceClass1 {
    public static void main(String args[]){
        Mouse d = new Mouse("a","123");
        System.out.println(d.getName());
        System.out.println(d.getId()); 
        d.eat();
        d.run();

        MouseChild c = new  MouseChild("childOfMouse","234");
        c.eat();
        c.run();

    }
}

class Mouse{
    private String name = "";
    private String id = "";

    //make a constructor
    public Mouse(String n,String i){
        setName(n);
        setId(i);
    }

    public void setName(String n){
        this.name = n;
    }

    public String getName(){
        return this.name;
    }
    public void setId(String id){
        this.id = id;
    }

    public String getId(){
        return this.id;
    }

    public void eat(){
        System.out.println("it is eating");
    }

    public void run(){
        System.out.println("it is running");
    }
}

// extends inherit
class MouseChild extends Mouse{
    public MouseChild(String n, String i){
        super(n,i);
    }
}