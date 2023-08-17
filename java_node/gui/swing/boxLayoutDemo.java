import java.awt.*;
import java.awt.Container;
import java.awt.desktop.AppHiddenListener;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.BoxLayout;

class boxLayoutDemo{
    public static void main(String[] args) {
        new boxLayoutDemo();
    }

    Container cp;
    JFrame jf;
    JRadioButton j1;
    JRadioButton j2;
    JRadioButton j3;

    JButton jb1;
    JButton jb2;
    JButton jb3;

    JPanel jp1;

    boxLayoutDemo(){
        jf = new JFrame();
        jf.setBounds(100, 100, 200, 300);

        jp1 = new JPanel();
        jp1.setSize(200,200);
        jp1.setBackground(Color.LIGHT_GRAY);


        // jf.getContentPane(); it will return a container
        cp = jf.getContentPane();
        cp.add(BorderLayout.CENTER,jp1);
        jp1.setLayout(new BoxLayout(jp1,BoxLayout.Y_AXIS));

        JPanel jp2 = new JPanel();
        jp2.setSize(200, 100);

        // ButtonGroup group = new ButtonGroup();
        j1 = new JRadioButton("one");
        j2 = new JRadioButton("two");
        j3 = new JRadioButton("three");

        // group.add(j1);
        // group.add(j2);
        // group.add(j3);
        // jp2.add(group);

        jp2.add(j1);
        jp2.add(j2);
        jp2.add(j3);
        jf.getContentPane().add(BorderLayout.SOUTH,jp2);
        j1.setSelected(true);

        jb1 = new JButton("AAA");
        Font f1 = new Font("Arial", Font.PLAIN,25);
        jb1.setFont(f1);
        jb1.setBackground(Color.yellow);

        jb2 = new JButton("BBB");
        Font f2 = new Font("Arial", Font.PLAIN,45);
        jb2.setFont(f2);
        jb1.setBackground(Color.red);

        jb3 = new JButton("CCC");
        Font f3 = new Font("Arial", Font.PLAIN,65);
        jb3.setFont(f3);
        jb3.setBackground(Color.green);

        jp1.add(jb1);
        jp1.add(jb2);
        jp1.add(jb3);

        jb1.setAlignmentX(Component.CENTER_ALIGNMENT);
        jb2.setAlignmentX(Component.CENTER_ALIGNMENT);
        jb3.setAlignmentX(Component.CENTER_ALIGNMENT);

        

        jf.setVisible(true);

        j1.addActionListener();
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}

class AddListener implements ActionListener{
    @Override
    public void actionPerformed(ActionListener e ){

    }
}
