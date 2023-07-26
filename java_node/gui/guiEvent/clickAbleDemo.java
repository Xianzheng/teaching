package guiEvent;
import java.awt.Color;
import java.awt.Frame;
import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class clickAbleDemo implements ActionListener,WindowListener{

    Frame f;
    Button b;

    public clickAbleDemo(){
        f = new Frame("test");
       
        f.setBounds(100, 100, 200, 200);
        f.addWindowListener(this);

        b = new Button("Press me");


        b.addActionListener(this);
      
        f.add(b,BorderLayout.NORTH);
        // f.add(b);
        f.setVisible(true);
    }

    public static void main(String args[]){
        new clickAbleDemo();
    }

    @Override
    public void windowOpened(WindowEvent e){}

    @Override
    public void windowClosing(WindowEvent e){
        System.exit(1);
    }
    
    @Override
	public void windowClosed(WindowEvent e) {}
    
    @Override
	public void windowIconified(WindowEvent e) {}
 

    @Override
	public void windowDeiconified(WindowEvent e) {}

    @Override
	public void windowActivated(WindowEvent e) {}
 
	@Override
	public void windowDeactivated(WindowEvent e) {}

    @Override
    public void actionPerformed(ActionEvent e){
        b.setBackground(Color.blue);
    }


   
   


    
    
}
