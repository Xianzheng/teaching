package thread;

public class threadSafetyDemo {

    public static void main(String[] args) {
        Dishes dishes = new Dishes();
        // kevin thread
        Thread kevin = new Thread(dishes, "Kevin");
        //justin thread
        Thread justin = new Thread(dishes, "Justin");

        justin.start();
        kevin.start();
       
    }
}

class Dishes implements Runnable{
    private int count = 1000; // you and justin have 20 dishes need to wash
    private int num = 0;// how many dishes washed
    @Override
    public void run(){

        while(true) {
            //if we don't have any more dishes we jump out the loop
            // problem: output show you and justin wash same dish in same time
            // reason: we meet thread safety problem, that means when thread kevin do the code
            //         between line 30 to 44 and don't finish and thread justin come int

            // to solve this probleam we nned to add a lock between line 30 to line 44
            // that means when you do the code justin need to wait,
            synchronized(this) {
                if(count <= 0){
                    break;
                }

                count --;
                num ++;

                // try{
                //     Thread.sleep(50);
                // }catch(InterruptedException e){
                //     e.printStackTrace();
                // }   
                System.out.println("washing dishes info:" + Thread.currentThread().getName()
                +" washing dishes number " + num  +" remains "+ count + " dishes ");
            }
        }
       

    }

}
/*
homework:
 * home work: use you knowleage to write buy tickes program,():
 * 
 * total tickes number : 10, there this three thread want to tickes
 * 
 * write the thread safety program to show how to order. 
 */
