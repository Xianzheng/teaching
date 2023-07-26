package gui;
import java.awt.Frame;
import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Panel;
import java.awt.CardLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent; 
public class CardLayoutDemo{
    Frame f = new Frame("CardLayout");
    String[] names = {"first","second","third","fourth","fifth"};
    

    public void init(){
        Panel p1 = new Panel();    
        CardLayout c = new CardLayout();
        p1.setLayout(c);
        for(int i =0; i< names.length; i++){
            p1.add(names[i],new Button(names[i]));
        }

        Panel p = new Panel();

        // control previous
        Button previous = new Button("previous");
        // add function to previous button
        previous.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0){
                c.previous(p1);
            }
        });

        // control next
        Button next = new Button("next");
        // add function to next button
        next.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0){
                c.next(p1);
            }
        });

        // control we just want to see first
        Button first = new Button("first One");
        first.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0){
                c.first(p1);
            }
        });

        p.add(previous);
        p.add(next);
        p.add(first);
        f.add(p1);
        f.add(p,BorderLayout.SOUTH);
        f.pack();
        f.setVisible(true);

    }
    public static void main(String[] args) {
       new CardLayoutDemo().init();
    }
}
/*
  hw
 * 1. write command about what's meaning for each line
 *  
 * 2. write your own version  cardlayoutDemo,  
 *    variable name makes more sense, you can not use the p,p1, p:viewPanel, p: buttonPanel
 *    to improve the readability
 * 
 */