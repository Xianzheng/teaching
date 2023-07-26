// java does not allow us to do inherited

// USB interface, mouse, key
public class classDemo extends classDemo2{

    public static void main(String[] args) {
        classDemo test = new classDemo();
        test.saySomeThing();
    }

    
}

class classDemo1 {

    int a = 10;
    int b = 20;

    
    public void saySomeThing(){
        System.out.println("Hello");
    }

}

class classDemo2 {

    int a = 10;
    int b = 20;

    
    public void saySomeThing(){
        System.out.println("Happy");
    }

}