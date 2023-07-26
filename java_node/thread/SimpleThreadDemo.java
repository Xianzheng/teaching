package thread;

public class SimpleThreadDemo {
    public static void main(String[] args) {
        System.out.println("This is a main thread");
        //call instance of class Mythread
        MyThread1 t1 = new MyThread1();
        t1.start();

        // make a instance of MyThread 2 will implement runable interface
        //pass this intance to Thread class, 
        //make a Thread instance to run it
        MyThread2 target = new MyThread2();
        Thread t2 = new Thread(target);
        t2.start();
    }
}

// method 1 , we can use extends(inheritance)

class MyThread1 extends Thread{

    @Override 
    public void run(){
        for (int i = 0; i < 5; i++){
            System.out.println("myThread11111   " + i );
        }
    }
}

// method2 , we use implements(interface) to make a Thread

class  MyThread2 implements Runnable{

    @Override
    public void run(){
        for (int i = 0; i < 5; i++){
            System.out.println("myThread22222   " + i );
        }
    }
}


// you have 10 books to read

// your brother have 10 books to read

// write a two thread to show who read first

// one use extends Thread(father class) way, other use implements Runable(interface) 



