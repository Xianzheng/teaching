package gui;
import java.awt.Button;
import java.awt.Color;
import java.awt.Frame;
import java.awt.GridLayout;


public class GridLayoutDemo {
    public static void main(String[] args) {
        
        Frame frame = new Frame("GridLayout");
        
        frame.setBounds(500, 500, 400, 300);

        GridLayout gl = new GridLayout(3,2,5,5);
        frame.setLayout(gl);


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

        frame.add(but1);
        frame.add(but2);
        frame.add(but3);
        frame.add(but4);
        frame.add(but5);

        frame.setVisible(true);

    }
}
