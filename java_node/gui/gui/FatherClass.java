
package gui;
public class FatherClass {
    //attribute for this class
    private String args1 = null;
    private String color = null;
    private String background = null;
    
    // constructor
    public FatherClass(String args1){
        this.args1 = args1;
    }

    //method
    public void setBackground(String background){
        this.background = background;
    }
    //method
    public void setColor(String color){
        this.color = color;
    }

    public String getColor(){
        return this.color;
    }

    

}
