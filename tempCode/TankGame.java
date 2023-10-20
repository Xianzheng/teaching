
import javax.swing.*;
import java.awt.*;




public class TankGame extends JFrame{
    Mypanel mp=null;

    public static void main(String[] args){
        // Tank t1=new Tank(3,3);

        // t1.x=10;
        // System.out.println(t1.getX());
        // t1.y=20;
        // System.out.println(t1.y);
        new TankGame();
        turnOnorDown(1);
        
    }
    static void turnOnorDown(int num){
        switch (num){
            case 0:
                System.out.println("This light is turned down");
                break;
            case 1:
                System.out.println("This light is turned on");
                break;

        }
    }
    public TankGame(){
        /*
         * we will add thread
         */
        mp=new Mypanel();

        this.add(mp);
        /*
         * we will add addKeyListener later
         * 
         */

         this.setSize(400, 300);
         this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         this.setVisible(true);
    }

    
}

class Mypanel extends Panel{
    
    Hero hero=null;
    public Mypanel(){
        hero=new Hero(100,100);
    }
    public void paint(Graphics g){
        super.paint(g);
        g.fillRect(0,0,400,300);
        
        if(hero.isLive){
            this.drawTank(hero.getX(),hero.getY(),g,hero.getDirect(),1);
        }

    }
    //how we can make our panelALLBITS
    //hw: draw the panel
    public void drawTank(int x,int y,Graphics g,int direct,int type){
        switch(type){
            case 0:
                g.setColor(Color.CYAN);
                break;
            case 1:
                g.setColor(Color.yellow);
                break;
        }
        switch (direct) {
            // up
            case 0:
                g.fill3DRect(x, y, 5, 30, false);
                g.fill3DRect(x + 5, y + 5, 10, 20, false);
                g.fill3DRect(x + 15, y, 5, 30, false);
                g.fillOval(x + 5, y + 10, 10, 10);
                g.drawLine(x + 10, y + 10, x + 10, y);
                break;
            // down
            case 1:
//                x = x + 50;
//                y = y + 50;
                g.fill3DRect(x, y, 5, 30, false);
                g.fill3DRect(x + 5, y + 5, 10, 20, false);
                g.fill3DRect(x + 15, y, 5, 30, false);
                g.fillOval(x + 5, y + 10, 10, 10);
                g.drawLine(x + 10, y + 10, x + 10, y + 30);
                break;
// left
            case 2:
//                x = x + 100;
//                y = y + 100;
                g.fill3DRect(x, y, 30, 5, false);
                g.fill3DRect(x + 5, y + 5, 20, 10, false);
                g.fill3DRect(x, y + 15, 30, 5, false);
                g.fillOval(x + 10, y + 5, 10, 10);
                g.drawLine(x + 10, y + 10, x, y + 10);
                break;
            // right
            case 3:
//                x = x + 150;
//                y = y + 150;
                g.fill3DRect(x, y, 30, 5, false);
                g.fill3DRect(x + 5, y + 5, 20, 10, false);
                g.fill3DRect(x, y + 15, 30, 5, false);
                g.fillOval(x + 10, y + 5, 10, 10);
                g.drawLine(x + 10, y + 10, x + 30, y + 10);
                break;
        }
    }

    
    
    
}

class Tank{
    int x=0;
    int y=0;

    int x2=0;
    int y2=0;

    int speed=2;
    int direct=0;

    int color;

    Boolean isLive = true;

    //set the lenght of the tank
    int sizeX=20;
    
    int sizeY=30;

    public Tank(int x,int y){
        this.x=x;
        this.y=y;
    }
    //make a method to set position X
    public void setX(int a){
        this.x=a;
    }
    //make a method to get position X
    public int getX(){
        return this.x;
    }

    public void setY(int b){
        this.y=b;
    }
    
    public int getY(){
        return this.y;
    }

    public void setSpeed(int b){
        this.speed=b;
    }
    
    public int getSpeed(){
        return this.speed;
    }

    public void setDirect(int b){
        this.direct=b;
    }
    
    public int getDirect(){
        return this.direct;
    }

    public void setSizeX(int b){
        this.sizeX=b;
    }
    
    public int getSizeX(){
        return this.sizeX;
    }

    public void setSizeY(int b){
        this.sizeY=b;
    }
    
    public int getSizeY(){
        return this.sizeY;
    }

    public void setColor(int color){
        this.color=color;
    }

    public int getColor(){
        return this.color;
    }
    //make method we have for tank
    public void moveUp(){
        this.y=this.y-this.speed;
    }

    public void moveDown(){
        this.y+=this.speed;
    }

    public void moveRight(){
        this.x+=this.speed;
    }

    public void moveLeft(){
        this.x-=this.speed;
    }

    public Boolean getIsLive(){
        return this.isLive;
    }

    public void setIsLive(boolean live){
        this.isLive=live;
    }

    //x,y is our tank's position. x2,y2 is our initial bullet position

    public int getX2(){
        switch(direct){
            case 0:
            case 1:
                x2=x+sizeX;
                break;
            case 2:
            case 3:
                x2=x+sizeY;
                break;
        }

        return x2;
    }
}
/*
 * homework:
 * define how tank move
 * 1.move up
 * 2.move down
 * 3.moveleft
 * 4.move right
 * 
 * remember we have speed
 * 
 * how we can get x2 and y2 deoends on(x and y)
 */

 /*
  * tank goes up if y goes up and it goes down if y goes down. if x goes up then it goes right if it goes down then the tank goes left.
  the speed is is how much x it travels so the more bigger it is then it will move further from the previous location.
  */

  //next we will build hero tank and enemy

  /*
   * Hw: 08/23/2023
   * try to practice switch
   * 
   * if you have a score, print A,B,C,D,F
   * 
   * >=90 is a
   * 80-89 is b
   * 70-79 is c
   * 60-69 is d
   * under 60 is f
   */

   /*
    * Hw: 08/23/2023
    *give me the text to explain how to tank move using method, try draw image  |TANK MOVEMENT|
    best way to explain is by making a instance of tank to print position

    *give me the text to explain how x2,y2 depends on x,y  try draw image       |BULLET MOVEMENT|
    best way: you can explain is to make a instance of tank to print position

    */

class Hero extends Tank{
    public Hero(int x,int y){
        super(x,y);
        super.setSpeed(6);

    }
}

class EnemyTank extends Tank{

    //do thread after
    //do shoot after

    public EnemyTank(int x,int y){
        super(x,y);
        
    }
}