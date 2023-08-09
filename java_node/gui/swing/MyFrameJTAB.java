package swing;
import java.awt.*;
import javax.swing.*;

public class MyFrameJTAB extends JFrame {
    /*
     * do some define in here, what component we will going to use
     */
    public static void main(String []args){
        new MyFrameJTAB();
    }
    
    JLabel jl1;
    JButton login, quit, register;
    JPanel jp1;
   
    JTabbedPane jtp;
    JPanel jp2,jp3,jp4;
    JLabel jl2, jl3,jl4,jl5;

    //addition
    JTextField jtf;
    JPasswordField jpf;
    JButton clear;



    public MyFrameJTAB(){

        super();
        //NORTH
        ImageIcon ic = new ImageIcon("./bird.jpg");
        jl1 = new JLabel(ic);
        //SOUTH PART
        jp1 = new JPanel();
        login = new JButton("LOGIN");
        quit = new JButton("QUIT");
        register = new JButton("REGISTER");
        jp1.add(login);
        jp1.add(quit);
        jp1.add(register);

        jtp = new JTabbedPane();
        jp2 = new JPanel();
        jp3 = new JPanel();
        jp4 = new JPanel();

        jp2.setBackground(Color.BLUE);


        jp3.setBackground(Color.RED);
        jp4.setBackground(Color.YELLOW);
        
        jtp.add("some number",jp2);
        jtp.add("email",jp3);
        jtp.add("phone number",jp4);

        this.add(jl1, BorderLayout.NORTH);
        this.add(jp1, BorderLayout.SOUTH);
        this.add(jtp, BorderLayout.CENTER);

        this.setVisible(true);
        this.setLocation(200, 200);
        this.setAlwaysOnTop(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();
        this.setTitle("some title");





    }
}

/*
 * hw:
 * add more gui on this JTabbedPame
 * 
 * use can try JTextField, JPassword 
 * 
 * (* just try )check the code before to implement some interface making button works
 *
 */
