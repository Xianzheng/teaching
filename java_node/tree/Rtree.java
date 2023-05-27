public class Rtree {


    static class Node{
        int value;
        Node left, right;

        public Node(int value){
            this.value = value;
            left = null;
            right = null;
        }
    }
    // automatically add node to a tree
    static void addNode(Node root, int value){
        
        if (value <= root.value){
            //add to root left
            if (root.left != null){
                addNode(root.left, value);
            }else{
                root.left = new Node(value);
            }
        }else{
            //add tp root right
            if (root.right != null){
                addNode(root.right, value);
            }else{
                root.right = new Node(value);
            }
        }
        
    }
    
    static void printTree(Node root){
        if(root != null){
            System.out.println(root.value);
            printTree(root.left);
            printTree(root.right);
        }
    }
    public static void main(String[] args) {
        Rtree tree = new Rtree();
        Node root = new Node(5);

        int[] tempValue = {4,2,5,6,10,5,6,8,1,23,45};
        for (int s: tempValue){
            tree.addNode(root, s);
        }

        /*
         * resurive to print this tree
         */
        tree.printTree(root);
        // System.out.println(root.value);
        // System.out.println(sample1.value);
        // System.out.println(sample3.value);
        // System.out.println(sample2.value);
        // System.out.println(sample4.value);


        
    }
}
