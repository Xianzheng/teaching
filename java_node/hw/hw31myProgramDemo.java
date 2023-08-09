import java.awt.Dimension;
import javax.swing.*;

public class hw31myProgramDemo extends JFrame{
    JSplitPane split1;
    JSplitPane split2;
    JSplitPane split3;
    JLabel label;
    JLabel label1;
    
    JLabel label2;
    JCheckBox checkbox1;
    JCheckBox checkbox2;
    JCheckBox checkbox3;
    JButton button1;
    JButton button2;
    JButton button3;
    JPanel panel1;
    JTextArea textarea1;
    JPanel panel2;
    public static void main(String[] args){
        new hw31myProgramDemo();
    }
    hw31myProgramDemo(){
        super("test");
        
        label=new JLabel("Youtube video");
        label1=new JLabel(new ImageIcon("testOIP.jpeg"));
        label1.setSize(600, 600);
        button1 = new JButton("Like");
        button2 = new JButton("Dislike");
        button3 = new JButton("Susbscribe");
        panel1 = new JPanel();
        textarea1=new JTextArea();
        panel2 = new JPanel();
        checkbox1=new JCheckBox(" ");
        checkbox2=new JCheckBox(" ");
        checkbox3=new JCheckBox(" ");
        panel2.add(textarea1);
        panel2.add(checkbox1);
        panel2.add(checkbox2);
        panel2.add(checkbox3);
        split1=new JSplitPane(JSplitPane.VERTICAL_SPLIT, label, label1);
        split2=new JSplitPane(JSplitPane.VERTICAL_SPLIT,panel1,panel2);
        
        split3=new JSplitPane(JSplitPane.VERTICAL_SPLIT, split1, split2);
        
        
        panel1.add(button1);
        panel1.add(button2);
        panel1.add(button3);
        
        split1.setOneTouchExpandable(true);
        //this.getContentPane().add(split1);
        this.getContentPane().add(split3);
        this.setLocation(100, 100);
        this.setSize(new Dimension(800, 800));
        this.setAlwaysOnTop(true);
        this.setResizable(false);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

}
}
/*
 * Homework:
 * make a file called myProgrameDemo
 * put a image on it(any)
 * under will be some password typing thhins where yoyu type a password(BUTTONS 3 ANY BUTTON NAME)
 * under that will be a description like content
 * under that will be 3 button
 * use swing or awt
 */