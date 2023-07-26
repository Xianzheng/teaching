package gui;
import java.awt.Frame;
import java.awt.Menu;
import java.awt.MenuBar;
import java.awt.MenuItem;

public class MenuDemo{

    private Frame f;
    public MenuDemo(){
        f = new Frame("test frame");

        f.setBounds(100,100,200,200);
        // menu can not directly add to frame
        // we need to set a MenuBar, MenuBar add a menu
        MenuBar mb = new MenuBar();
        f.setMenuBar(mb);

        //we make some menu add to menuBar
        Menu m1 = new Menu("File");
        
        Menu m2 = new Menu("Edit");

        Menu m3= new Menu("Help");

        mb.add(m1);
        mb.add(m2);
        mb.add(m3);

        //we make some some menuItem add to Menu
        MenuItem mi1 = new MenuItem("Save");
        MenuItem mi2 = new MenuItem("Load");
        MenuItem mi3 = new MenuItem("Quit");

        m1.add(mi1);
        m1.add(mi2);
        m1.addSeparator();
        m1.add(mi3);

        f.setVisible(true);
    }

    public static void main(String[] args) {
        new MenuDemo();
    }
}
/*
 * hw:
 * 
 * add some menu item to menu edit
 * 
 * implement window lister we can click close button，  in frame to exit frame
 */