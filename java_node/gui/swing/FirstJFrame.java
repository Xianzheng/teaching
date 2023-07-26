package swing;
import java.awt.Color;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class FirstJFrame extends JFrame{
    
    
	public static void main(String[] args) {
        new FirstJFrame();
    }

    public FirstJFrame(){
        super();
        this.setBounds(100, 100, 200, 200);

        JPanel jp = new JPanel();
        jp.setSize(100, 100);
        jp.setBackground(Color.blue);
        this.getContentPane().setLayout(null);
        this.getContentPane().add(jp);

        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

}

/*
 * MAKE Actionlistener WORKS (code)
 * TRY TO READ TEXT ADITER
 * CONPARE AND CONTRAST FirtJFrame.java and FirstFrame(text about how you understand)
 */