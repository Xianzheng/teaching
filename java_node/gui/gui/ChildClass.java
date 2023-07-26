package gui;

public class ChildClass extends FatherClass {
    /*
     * when Father class have contructor,
     * when ChildClass extends FatherClass,
     * we must buld contructor , contructor must have the same parameter
     */

    public ChildClass(String args1) {
        super(args1);
        
    }

    public static void main(String[] args) {
        ChildClass cc = new ChildClass("H1");

        cc.setColor("blue");
        cc.setBackground("red");
        System.out.println(cc.getColor());

    }

}
// hw , write some code to pracitice

//write a simple gui, size ,background, color, depends on you as long as you can make code code works;

// write a father class must have contrutor, a child class extends fater class, make some functionality to implement.
