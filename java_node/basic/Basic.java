package basic;

//modifier
//public
//private
//default
//protected
//static is a key word

//void is return type

//main is method name

//java objected oritend language

//sometimes a java progame will use aother java program, we need to differ the modifer
//object-oriented
public class Basic {

    private static void methodname1(){
        System.out.println("This is from methodname1");
    }

    static int methodname2(){
        return 1;
    }


    public static void main(String args[]){
        System.out.println("Test");
        methodname1();
        System.out.print(methodname2());
    }
    
}
