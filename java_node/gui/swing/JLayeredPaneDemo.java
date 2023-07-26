package swing;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLayeredPane;
import javax.swing.JPanel;
import javax.swing.WindowConstants;

public class JLayeredPaneDemo extends JFrame{

    public static void main(String[] args) {
        new JLayeredPaneDemo();
    }

    public JLayeredPaneDemo(){
        super("JLayeredPane test");
        this.setSize(300, 300);
        this.setLocationRelativeTo(null);
        JLayeredPane layeredPane = new JLayeredPane();


        JPanel jp1 = new JPanel();
        jp1.setBounds(30, 30, 100, 100);
        jp1.setBackground(Color.blue);
        layeredPane.add(jp1, 0);

        JPanel jp2 = new JPanel();
        jp1.setBounds(60, 60, 100, 100);
        jp1.setBackground(Color.red);
        layeredPane.add(jp2, 2);

        JPanel jp3 = new JPanel();
        jp1.setBounds(90, 90, 100, 100);
        jp1.setBackground(Color.green);
        layeredPane.add(jp3, 1);

        this.getContentPane().add(layeredPane);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);





    }
    
}
