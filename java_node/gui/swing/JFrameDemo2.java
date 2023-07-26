package swing;

import java.awt.Dimension;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JSplitPane;

public class JFrameDemo2 extends JFrame{

    JSplitPane jsp;
    JList<String> jlist;
    JLabel j1;
    
    public static void main(String[] args) {
        new JFrameDemo2();
    }

    JFrameDemo2(){
        super("test");
        String[] words = {"boy","girl","one","bird"};

        jlist = new JList<String>(words);
        j1 = new JLabel(new ImageIcon("./bird.jpg"));

        jsp = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT,jlist,j1);
        jsp.setOneTouchExpandable(true);
        this.getContentPane().add(jsp);
        this.setLocation(100,100);

        this.setSize(new Dimension(300, 300));
        this.setAlwaysOnTop(true);
        this.setResizable(false);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


    }
    
}
