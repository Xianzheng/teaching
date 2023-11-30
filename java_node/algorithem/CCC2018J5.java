import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.Scanner;

public class CCC2018J5 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int totalPages = scanner.nextInt();

        // make input for this question

    }

    // recursive method : write your command by reading this method carefully
    /*
     * find end recursive
     * what we changed for parameters
     * find what is return
     * find the goal for this method
     */
    public static void getReachablePages(Node node, Set<Integer> pages) {
        if (!pages.contains((node.value))) {
            pages.add(node.value);
            for (Node child : node.chidren) {
                getReachablePages(child, pages);
            }
        }
    }

    // recursive method : write your command by reading this method carefully
    /*
     * find end recursive
     * what we changed for parameters
     * find what is return
     * find the goal for this method
     */
    public static int findShortestPath(List<Node> nodesToCheck, int level) {
        level += 1;
        List<Node> childNodes = new ArrayList<>();
        for (Node node : nodesToCheck) {
            if (node.chidren.size() == 0) {
                return level;
            } else {
                for (Node child : node.chidren) {
                    childNodes.add(child);
                }
            }
        }
        return findShortestPath(childNodes, level);
    }

}

class Node {
    int value;

    List<Node> chidren;

    public Node(int value) {
        this.value = value;
    }
}