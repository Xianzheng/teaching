public class Node {
    int value;
    Node next;
    //this 
    public Node(int inp){
        this.value = inp;
        this.next = null;
    }

    public autoAdd(){

    }
    public static void main(String[] args) {
     
        
        Node a = new Node(0);
        a.autoAdd(1);
        a.autoAdd(2);
        // Node b = new Node(1);
        // Node c = new Node(2);
        // a.next = b;
        // b.next = c;

        System.out.print(a.next.next.value);
        
    }

    /*
     * use your knowledge to build a basic linkedlist , it contains at least 5 Node like the demon code in class
     * advanced part how to build autoAdd method
     * hint you can think with recursive, or you just use while loop
     */
}
