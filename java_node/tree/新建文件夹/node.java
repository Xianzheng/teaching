package recursive;

import java.util.*;

public class node {
    int value;//inner attribute of the node
    node left;
    node right;
    public node(int value){
        this.value=value;
        this.left=null;
        this.right=null;

    }
    public static void autoAdd(node a, int value){//this is recursive way
        if (value<=a.value){
            if (a.left!=null){
                autoAdd(a.left, value);
            }else{
                a.left=new node(value);
            }
        }else{
            if (a.right!=null){
                autoAdd(a.right, value);
            }else{
                a.right=new node(value);
            }
        }
        
    }
    public static void addNext(node a,int value){//this is while loop way
        
        while(a.left!=null){
            a=a.left;
        }
        a.left=new node(value);
    }
    public static void printlst(node a){
        //System.out.println(a.value);
        
        if (a.right!=null){
            System.out.println(a.value);
            System.out.println(a.left.value);
            System.out.println(a.right.value);
            }
            //a=a.left;
            //System.out.println(a.value);
        
       
        
    }
    // write the command for BFS, show me how do you  think for BFS works, for next class we will talk about interface
    //A a = new A() this A is a clss
   // A a = new B() this A id a interface
    public static List<Integer> BFS(node root){
        //interface
        Queue<node> queue = new LinkedList<>();
        queue.add(root);
        List<Integer> result = new ArrayList<>();

        while(!queue.isEmpty()){
            node treeNode = queue.poll();
            result.add(treeNode.value);

            if(treeNode.left != null){
                queue.add(treeNode.left);
            }

            if(treeNode.right != null){
                queue.add(treeNode.right);
            }

        }

        return result;
    }
    //DFS
    public static void autoPrint(node a){
        //System.out.println(a.value);
        if(a!=null){
            
            autoPrint(a.left);
            
            autoPrint(a.right);
            System.out.println(a.value);
        }
    }
    public static void main(String[] args){//this is a general tree
       
       node hw=new node(5);
       //node hw1=new node(5);
       //a.autoaAdd(i) this adds 1 to a likedlist
       //hint for autoadd: you can think with recusrive or use while loop
       autoAdd(hw, 3);
       autoAdd(hw, 8);
       autoAdd(hw, 1);
       autoAdd(hw, 4);
       autoAdd(hw, 6);
       autoAdd(hw, 10);
    //    autoPrint(hw);
       List<Integer> result = BFS(hw);
       System.out.println(result);
       

       //addNext(hw1, 2);
       //System.out.println(hw1.left.value);
       //System.out.println(a.left.value);
       //System.out.println(b.left.value);
       //System.out.println(hw.value); //this is with recursive way 
    //    autoAdd(hw, 3);
    //    //System.out.println(hw.left.value);
    //    autoAdd(hw, 19);
    //    //System.out.println(hw.left.left.value);
    //    autoAdd(hw, 200);
    //    //System.out.println(hw.left.left.left.value);
    //    autoAdd(hw, 17);
    //    //System.out.println(hw.left.left.left.left.value);
    //    //printlst(hw);
    //    autoPrint(hw);
       
    }
}

//hw: use your knowledge to build a basic linkedlist, it contains at least 5 node like tge demo in this class
//advanced part how to build a autoAdd method.

//new hw: make a binary tree (recursive way basically) so there is a node and if the next node is smaller it goes before if not it goes after and this continues.