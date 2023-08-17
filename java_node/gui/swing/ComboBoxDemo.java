
package swing;
import java.awt.*;
import javax.swing.*; 
public class ComboBoxDemo extends JFrame{

    public static void main(String[] args) {
        new ComboBoxDemo();
    }
    
    
    JComboBox<String> cb;
    JList<String> jl;
    JScrollPane jsp;

    public ComboBoxDemo(){
        String[] city = {"Montreal","Toronto","Guelph"};

        String[] r = {"a","b","c","d","e"};

        cb = new JComboBox<String>(city);
        jl = new JList<String>(r);
        jsp = new JScrollPane(jl);

        this.add(cb);
        this.add(jsp);

        this.setVisible(true);



    }
}
