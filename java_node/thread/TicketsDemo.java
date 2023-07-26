package thread;
public  class  TicketsDemo  {

    public static void main(String[] args) {
        MyThread myThread = new MyThread();
        new Thread(myThread).start();
        new Thread(myThread).start();
        new Thread(myThread).start();
    }
}

class MyThread implements Runnable {
    private static int ticket = 100;
    @Override
    public void run() {
        while (ticket>0){
            show();
        }
    }

    private synchronized void show(){
        if(ticket>0){
            System.out.println(Thread.currentThread().getName()+"+++++++++"+ticket);
            ticket--;
        }

    }
}
