package swing;

import java.awt.FlowLayout;
import java.awt.GridLayout;

import javax.swing.*;


public class JCheckBox1 extends JFrame{
    JCheckBox jcb1,jcb2,jcb3;
    JRadioButton jrb1,jrb2;
    JLabel jl1,jl2;
    JButton jb1,jb2;
    JPanel jp1,jp2,jp3;
    
    public JCheckBox1(String title){
        super(title);
        jcb1=new JCheckBox("football");
        jcb2=new JCheckBox("basketball");
        jcb3=new JCheckBox("pingpong");

        jrb1=new JRadioButton("male");
        jrb2=new JRadioButton("female");

        jl1=new JLabel("Favorite Sport?");
        jl2=new JLabel("Gender?");

        jb1=new JButton("submit");
        jb2=new JButton("cancel");

        jp1=new JPanel(new FlowLayout());
        jp2=new JPanel(new FlowLayout());
        jp3=new JPanel(new FlowLayout());

        jp1.add(jl1);
        jp1.add(jcb1);
        jp1.add(jcb2);
        jp1.add(jcb3);

        jp2.add(jl2);
        jp2.add(jrb1);
        jp2.add(jrb2);

        jp3.add(jb1);
        jp3.add(jb2);

        this.setLayout(new GridLayout(3,1, 5, 5));
        this.add(jp1);
        this.add(jp2);
        this.add(jp3);
        this.setAlwaysOnTop(true);
        this.setSize(500, 500);
        this.setResizable(false);
        this.setVisible(true);
        this.setLocation(200,200);
        this.pack();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main(String[] orgs){
        new JCheckBox1("test");
    }
}
