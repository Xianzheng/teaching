package gui;
import java.awt.*;

public class ComponentsDemo {

    public static void main(String[] args) {
        Frame frame = new Frame("component demo ");
        frame.setBounds(100,100,600,300);

        GridLayout gl = new GridLayout(4,2,5,5);
        frame.setLayout(gl);

        // components button
        Button but1 = new Button("button");
        Panel pn0 = new Panel();
        pn0.setLayout( new FlowLayout());
        pn0.add(but1);
        frame.add(pn0);

        //components checkbox
        Panel pn1 = new Panel();
        pn1.setLayout( new FlowLayout());
        pn1.add(new Checkbox("one",null,true));
        pn1.add(new Checkbox("two"));
        pn1.add(new Checkbox("three"));
        frame.add(pn1);

        //components checkboxgroup
        Panel pn2 = new Panel();
        CheckboxGroup cg = new CheckboxGroup();
        pn2.setLayout( new FlowLayout());
        pn2.add(new Checkbox("one",cg,true));
        pn2.add(new Checkbox("two",cg,false));
        pn2.add(new Checkbox("three",cg,false));
        frame.add(pn2);

        // components choice 
        Choice c = new Choice();
        c.add("red");
        c.add("green");
        c.add("yello");
        frame.add(c);

        // components textField

        Panel pn3 = new Panel();
        pn3.setLayout( new FlowLayout());
        TextField tf = new TextField("",30);
        pn3.add(tf);
        frame.add(pn3);

        // components Textarea

        TextArea ta = new TextArea();
        frame.add(ta);

        frame.setVisible(true);
    }
    
}
/*
 * design a gui, add 4 components, more is better, choose your layout
 * choose to do J3 OR J4
 * LINK: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2020/ccc/juniorEF.pdf
 */
