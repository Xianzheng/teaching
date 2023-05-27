/*
 * how many you understand for this code
 * show the command for each line
 * CCC 2019, J5 at: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
 */
public class Tree {
    static class Node{
        int value;
        Node left, right;
        Node(int value){
            this.value = value;
            left = null;
            right = null;
        }
    }

    public void insert(Node node, int value){
        if(value <= node.value){
            if (node.left != null){
                insert(node.left,value);
            }else{
                System.out.println(" Inserted " + value + " to left of " + node.value); 
                node.left = new Node(value);
            }
        }else{
            if (node.right != null){
                insert(node.right,value);
            }else{
                System.out.println(" Inserted " + value + " to right of " + node.value); 
                node.right = new Node(value);
            }
        }
    }

    public void traverseInOrder(Node node){
        if (node != null){
            traverseInOrder(node.left);
            System.out.println(" "+node.value);
            traverseInOrder(node.right);
        }
    }
    public static void main(String[] args) {
        Tree tree = new Tree();
        Node root = new Node(5);
        System.out.println("Start to build tree");
        tree.insert(root,2);
        tree.insert(root,4);
        tree.insert(root,8);
        tree.insert(root,6);
        tree.insert(root,7);
        tree.insert(root,3);
        tree.insert(root,9);
        tree.traverseInOrder(root);

    }
}
