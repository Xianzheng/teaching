package gui;
import java.awt.Color;
import java.awt.Frame;
import java.awt.Panel;;

public class FirstFrame extends Frame {

    public static void main(String[] args) {
        FirstFrame fr = new FirstFrame("Hello");
        fr.setSize(240,240);
        fr.setBackground(Color.green);
        // cancel the default layout for frame
        fr.setLayout(null);
        Panel panel = new Panel();
        //(english version ）chinese  version
        panel.setSize(100,100);
        panel.setBackground(Color.yellow);
        fr.add(panel);
        fr.setVisible(true);
        
    }

    public FirstFrame(String str){
        super(str);// we want to initialize fater class' attribute
    }
    
}

/*
 * hw:
 * 
 * write code
 * 
 * show me you understand how to generic
 * 
 * show me me make multiple thread works
 * 
 * add more panels to main frame
 */
