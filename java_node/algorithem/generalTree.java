import java.util.ArrayList;
import java.util.LinkedList;

public class generalTree {

    public static void main(String[] args) {
        Node root = new Node(0);

        Node leaf1 = new Node(1);
        Node leaf2 = new Node(2);
        Node leaf3 = new Node(3);

        root.chilldren.add(leaf1);
        root.chilldren.add(leaf2);
        root.chilldren.add(leaf3);

        Node leaf4 = new Node(4);
        Node leaf5 = new Node(5);

        leaf1.chilldren.add(leaf4);
        leaf1.chilldren.add(leaf5);

        Node leaf6 = new Node(6);
        Node leaf7 = new Node(7);

        leaf3.chilldren.add(leaf6);
        leaf3.chilldren.add(leaf7);

        // DFS(root);

        BFS(root);

    }

    static void printTree(Node n) {
        System.out.println(n.val);

        if (n.chilldren.size() != 0) {

            for (Node i : n.chilldren) {

                printTree(i);
            }
        }

    }

    // static void TRY(Node n){
    // ArrayList<Node> queue = new ArrayList<>();
    // int count = 0;

    // for (Node q : queue){
    // if(q.val == 2){
    // count += 1;
    // }
    // }

    // if(count > 0){

    // }else{

    // }
    // }
    static void DFS(Node n) {
        ArrayList<Node> queue = new ArrayList<>();
        queue.add(n);

        while (queue.size() != 0) {
            Node t = queue.remove(queue.size() - 1);

            for (Node i : t.chilldren) {
                queue.add(i);
            }
            System.out.println(t.val);

        }

    }

    // Breadth First Search
    static void BFS(Node n) {
        ArrayList<Node> queue = new ArrayList<>();
        queue.add(n);

        while (queue.size() != 0) {
            Node t = queue.remove(0);

            for (Node i : t.chilldren) {
                queue.add(i);
            }
            System.out.println(t.val);

        }

    }

}

class Node {
    int val = 0;
    ArrayList<Node> chilldren = new ArrayList<>();

    public Node(int val) {
        this.val = val;

    }
}