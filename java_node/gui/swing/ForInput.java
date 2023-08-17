package swing;
import java.awt.*;
import java.awt.event.*;
import java.awt.event.ActionListener;

import javax.swing.*;

public class ForInput extends JFrame{

    public static void main(String[] args) {
        new ForInput("input");
    }

    public ForInput(String name){
        super(name);
        
        JPanel jp1 = new JPanel();
        JLabel jl1 = new JLabel("USER NAME");
        JTextField username = new JTextField(10);

        jp1.setLayout(new FlowLayout());
        jp1.add(jl1);
        jp1.add(username);

        JPanel jp2 = new JPanel();
        JLabel jl2 = new JLabel("PASSWORD");
        JPasswordField pw = new JPasswordField(10);

        pw.setEchoChar('*');
        jp2.setLayout(new FlowLayout());
        jp2.add(jl2);
        jp2.add(pw);

         JPanel jp3 = new JPanel();
         JButton ok = new JButton("SUBMIT");
         JButton cancel = new JButton("CANCEL");

         ok.addActionListener(new ActionListener() {
            
            public void actionPerformed(ActionEvent arg0){
                System.out.println("this can be clicked");
                System.out.println(username.getText());
                System.out.println(pw.getText());
                
            }
         });

         jp3.setLayout(new FlowLayout());
         jp3.add(ok);
         jp3.add(cancel);

         this.setLayout(new GridLayout(3,1));

        this.add(jp1);
        this.add(jp2);
        this.add(jp3);
        this.setAlwaysOnTop(true);
        this.setSize(500,300);
        this.setResizable(false);
        this.setVisible(true);
        this.setLocation(200,200);
        this.pack();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
         // set frame with grid layout
         // make frame show
         // make frame clost button can be cliked
         // make frame can not resize


    }
    
}
