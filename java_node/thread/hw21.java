public class hw21 {
    public static void main(String[] args){
        kevin first=new kevin();
        first.start();
        justin target=new justin();
        Thread second=new Thread(target);
        
        second.start();
    }
}
class kevin extends Thread{
    @Override
    public void run(){
        for(int i=0;i<10;i++){
            System.out.println("Kevin "+ i);
        }
    }
}

class justin implements Runnable{
    @Override
    public void run(){
        for(int i=0;i<10;i++){
            System.out.println("Justin "+ i);
        }
    }
}




//hw: you have 10 books to read
//your brother have 10 book to read

//write two thread to show who reads the book first

//one thread uses extend, the other one will use implement