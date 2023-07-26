package thread;
//interface, generic, thread, gui

//we try to make a real program

public class threadDemo {
    public static void main(String[] args) {
        // System.out.println("Hello");
        RunnableDemo r1 = new RunnableDemo("Thread-1");
        r1.start();
        RunnableDemo r2 = new RunnableDemo("Thread-2");
        r2.start();

    }
}

class RunnableDemo implements Runnable{
    //inorder to let our multiple thread works
    //we need to implements Runable interface
    // we all need to override two method one is run(), and another is start
    private Thread t;
    private String threadName;
   
    RunnableDemo(String name){
        threadName = name;
    }
    
    public void run(){
        System.out.println("running "+ threadName);
        
        for (int i = 4 ; i > 0; i -- ){
            System.out.println("running "+ threadName + "," + i);
            
        }
        System.out.println("");
       
    }
      
    public void start(){
         System.out.println("starting "+ threadName);
         
        t = new  Thread(this,threadName);
        t.start();
         
    }
    
}