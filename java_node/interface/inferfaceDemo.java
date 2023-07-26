public class inferfaceDemo implements mouseInterface, keyboradInterface{
    public void printMouse(){
        System.out.println("this is mouse");
    }

    public void printKeyBoard(){
        System.out.println("keyboard");
    }

    public static void main(String[] args) {
        mouseInterface mouse = new inferfaceDemo();
        mouse.printMouse();
        keyboradInterface keyboard = new inferfaceDemo();
        keyboard.printKeyBoard();
    }
}

interface mouseInterface{
    int a = 0;
    //abstract method , you only need to give the name of method you don't need to real implement it
    public void printMouse();
}

interface keyboradInterface{
    //abstract method
    public void printKeyBoard();
}

