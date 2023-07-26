package gui;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Panel;
import java.awt.BorderLayout;
import java.awt.Button;

public class BorderLayoutDemo {
     public static void main(String[] args) {
        Frame frame = new Frame("Flow Out");
        frame.setBounds(500, 500, 400, 300);


        Button but1 = new Button("button1");
        Button but2 = new Button("button2");
        Button but3 = new Button("button3");
        Button but4 = new Button("button4");
        Button but5 = new Button("button5");

        but1.setBackground(Color.blue);
        but2.setBackground(Color.yellow);
        but3.setBackground(Color.red);
        but4.setBackground(Color.green);
        but5.setBackground(Color.pink);

        frame.add(but1,BorderLayout.EAST);
        frame.add(but2,BorderLayout.NORTH);
        frame.add(but3,BorderLayout.SOUTH);
        frame.add(but4,BorderLayout.WEST);
        frame.add(but5);

        frame.setVisible(true);
        

    }
}

// CARD LAYOUT
// GRID BAG LAYOUT
/*
 *  HW:
 * COMPARE AND CONTRAST FLOW LAYOUT AND BORDERLAY OUT
 * EXPALIN IN TEXT AND CODING
 */
