import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Vector;

public class Tank0321 extends JFrame {
    MyPanel mp = null;
    public static void main(String[] args) {
        Tank0321 start = new Tank0321();
    }

    public Tank0321() {
        mp = new MyPanel();
        Thread thread = new Thread(mp);
        thread.start();
        this.add(mp);
        this.addKeyListener(mp);
        this.setSize(400, 300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

}

class MyPanel extends JPanel implements KeyListener, Runnable {

    Hero hero = null;
    // 敌人坦克的初始数量
    int enSize = 3;
    // 敌人总数量
    int enemyTankTotal = 5;
    // 我方总数量
    int heroTotal = 1;
    // 敌人坦克的集合
    Vector<EnemyTank> ets = new Vector<EnemyTank>();
    // 子弹
    HeroShot heroShot = null;
    // 三张图片，组成爆炸效果
    Image image1 = null;
    Image image2 = null;
    Image image3 = null;
    // 炸弹
    Vector<Bomb> bombs = new Vector<Bomb>();


    public MyPanel() {
        hero = new Hero(100, 200);
        for (int i = 0; i < enSize; i++) {
            EnemyTank et = new EnemyTank((i + 1) * 50, 0);
            et.setDirect(1);
            Thread thread = new Thread(et);
            thread.start();
            ets.add(et);
        }
        image1 = Toolkit.getDefaultToolkit().getImage(MyPanel.class.getResource("./bomb_1.gif"));
        image2 = Toolkit.getDefaultToolkit().getImage(MyPanel.class.getResource("./bomb_2.gif"));
        image3 = Toolkit.getDefaultToolkit().getImage(MyPanel.class.getResource("./bomb_3.gif"));
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        g.fillRect(0, 0, 400, 300);
        // 画我方tank
        if (hero.isLive) {
            this.drawTank(hero.getX(), hero.getY(), g, hero.getDirect(), 1);
        }
        // 画我方子弹
        for (int i = 0; i < hero.heroShots.size(); i++) {
            HeroShot heroShot = hero.heroShots.get(i);
            if (heroShot.isLive) {
                this.drawShot(heroShot.getX(), heroShot.getY(), g, heroShot.getDirect(), 1);
                // 是否击中敌人
                for (int j = 0; j < this.ets.size(); j++) {
                    EnemyTank enemyTank = this.ets.get(j);
                    if (!enemyTank.isLive) continue;
                    Boolean isHit = this.hitTank(heroShot, enemyTank);
                    if (isHit) {
                        System.out.println(1111);
                        enemyTank.setIsLive(false);
                        heroShot.setIsLive(false);
                        this.ets.remove(enemyTank);
                        this.bombs.add(new Bomb(enemyTank.getX(), enemyTank.getY()));
                        // 敌人复活
                        if (enemyTankTotal > 0) {
                            EnemyTank enemyTank1 = new EnemyTank(100, 20);
                            enemyTank1.setDirect(1);
                            Thread thread = new Thread(enemyTank1);
                            thread.start();
                            this.ets.add(enemyTank1);
                            enemyTankTotal--;
                        } else {
                        // 敌人全死，胜利！！！
                        }

                    }
                }
            } else {
                hero.heroShots.remove(heroShot);
            }
        }

        // 画敌方tank
        for (int i = 0; i < ets.size(); i++) {
            EnemyTank et = ets.get(i);
            // 判断tank重叠
//            for (int k = 0; k < ets.size(); k++) {
//                EnemyTank et2 = ets.get(k);
//                // 重叠，则改变方向
//                if (this.tankOverlop(et, et2)) {
//                    System.out.println("cd" + et.x + et.y);
//                    System.out.println("cd2" + et2.x + et2.y);
//                    // 同一条线上
//                    if ((et.direct == 0 || et.direct == 1) && (et2.direct == 0 || et2.direct == 1)) {
//                        if (et.direct == 0) {
//                            et.setDirect(1);
//                            et2.setDirect(0);
//                        } else {
//                            et.setDirect(0);
//                            et2.setDirect(1);
//                        }
//
//                    } else if ((et.direct == 2 || et.direct == 3) && (et2.direct == 2 || et2.direct == 3)) {
//                        if (et.direct == 2) {
//                            et.setDirect(3);
//                            et2.setDirect(2);
//                        } else {
//                            et.setDirect(2);
//                            et2.setDirect(3);
//                        }
//                    // 不同线上，垂直方向
//                    } else  {
//                        switch (et.direct) {
//                            case 0:
//                                et.setDirect(1);
//                                break;
//                            case 1:
//                                et.setDirect(0);
//                                break;
//                            case 2:
//                                et.setDirect(3);
//                                break;
//                            case 3:
//                                et.setDirect(2);
//                                break;
//                        }
//                        switch (et2.direct) {
//                            case 0:
//                                et2.setDirect(1);
//                                break;
//                            case 1:
//                                et2.setDirect(0);
//                                break;
//                            case 2:
//                                et2.setDirect(3);
//                                break;
//                            case 3:
//                                et2.setDirect(2);
//                                break;
//                        }
//                    }
//                }
//            }
            this.drawTank(et.getX(), et.getY(), g, et.getDirect(), 0);
            // 画敌方子弹
            for (int j = 0; j < et.enemyShots.size(); j++) {
                EnemyShot enemyShot = et.enemyShots.get(j);
                if (enemyShot.isLive) {
                    this.drawShot(enemyShot.getX(), enemyShot.getY(), g, enemyShot.getDirect(), 1);
                    Boolean isHit = this.hitTank(enemyShot, hero);
                    if (isHit) {
                        hero.setIsLive(false);
                        enemyShot.setIsLive(false);
                        System.out.println("我方tank挂了");
                        this.bombs.add(new Bomb(hero.getX(), hero.getY()));
                        // 我方复活
                        if (heroTotal > 0) {
                            hero.setIsLive(true);
                            hero.setX(150);
                            hero.setY(220);
                            heroTotal--;
                        } else {
//                             我方没命了，失败！！！
                        }
                    }
                } else {
                    et.enemyShots.remove(enemyShot);
                }
            }
        }

        // 画出炸弹
        for (int i = 0; i < bombs.size(); i++) {
            Bomb bomb = bombs.get(i);
            if (bomb.life > 6) {
                g.drawImage(image1, bomb.getX(), bomb.getY(), 30, 30, this);
            } else if (bomb.life > 3) {
                g.drawImage(image2, bomb.getX(), bomb.getY(), 30, 30, this);
            } else {
                g.drawImage(image3, bomb.getX(), bomb.getY(), 30, 30, this);
            }
            bomb.lifeDown();
            if (!bomb.isLive) {
                bombs.remove(bomb);
            }

        }
//        this.drawTank(hero.getX(), hero.getY(), g, hero.getDirect(), 0);
//        this.drawTank(hero.getX(), hero.getY(), g, hero.getDirect(), 1);
//        this.drawTank(hero.getX(), hero.getY(), g, hero.getDirect(), 0);
    }

    // 判断是否击中敌人
    public Boolean hitTank(Shot shot, Tank tank) {
        int tankX = tank.getX();
        int tankY = tank.getY();
        int shotX = shot.getX();
        int shotY = shot.getY();
        int tankX2 = 0;
        int tankY2 = 0;
        switch (tank.direct) {
            case 0:
            case 1:
                tankX2 = tankX + 20;
                tankY2 = tankY + 30;
                break;
            case 2:
            case 3:
                tankX2 = tankX + 30;
                tankY2 = tankY + 20;
                break;
        }
//        System.out.println(tankX);
//        System.out.println(tankY);
//        System.out.println(shotX);
//        System.out.println(shotX);
//        System.out.println(shotX);
//        System.out.println(shotX);
        if (tankX <= shotX && shotX <= tankX2 && tankY <= shotY && shotY <= tankY2) {
            return true;
        } else {
            return false;
        }
    }

    // 判断tank是否重叠
    public Boolean tankOverlop(Tank tank1, Tank tank2) {
        if (tank1.x <= tank2.getX2() && tank1.getX2() >= tank2.x && tank1.y <= tank2.getY2() && tank1.getY2() >= tank2.y) {
            return true;
        } else {
            return false;
        }
    }

    // 画坦克
    public void drawTank(int x, int y, Graphics g, int direct, int type) {
        switch (type) {
            case 0 :
                g.setColor(Color.CYAN);
                break;
            case 1 :
                g.setColor(Color.yellow);
                break;
        }

        switch (direct) {
            // 上
            case 0:
                g.fill3DRect(x, y, 5, 30, false);
                g.fill3DRect(x + 5, y + 5, 10, 20, false);
                g.fill3DRect(x + 15, y, 5, 30, false);
                g.fillOval(x + 5, y + 10, 10, 10);
                g.drawLine(x + 10, y + 10, x + 10, y);
                break;
            // 下
            case 1:
//                x = x + 50;
//                y = y + 50;
                g.fill3DRect(x, y, 5, 30, false);
                g.fill3DRect(x + 5, y + 5, 10, 20, false);
                g.fill3DRect(x + 15, y, 5, 30, false);
                g.fillOval(x + 5, y + 10, 10, 10);
                g.drawLine(x + 10, y + 10, x + 10, y + 30);
                break;
            // 左
            case 2:
//                x = x + 100;
//                y = y + 100;
                g.fill3DRect(x, y, 30, 5, false);
                g.fill3DRect(x + 5, y + 5, 20, 10, false);
                g.fill3DRect(x, y + 15, 30, 5, false);
                g.fillOval(x + 10, y + 5, 10, 10);
                g.drawLine(x + 10, y + 10, x, y + 10);
                break;
            // 右
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

    // 画子弹
    public void drawShot(int x, int y, Graphics g, int direct, int type) {
        switch (type) {
            case 0 :
                g.setColor(Color.CYAN);
                break;
            case 1 :
                g.setColor(Color.yellow);
                break;
        }
        g.fillOval(x, y, 4, 4);

    }


    @Override
    public void keyTyped(KeyEvent e) {
//        System.out.println("01");
    }

    @Override
    public void keyPressed(KeyEvent e) {
//        System.out.println('press key');
//        System.out.println("11");

        // 移动坦克
        switch (e.getKeyCode()){
            case KeyEvent.VK_UP:
            case KeyEvent.VK_W:

                hero.moveUp();
                hero.setDirect(0);
                break;
            case KeyEvent.VK_DOWN:
            case KeyEvent.VK_S:

                hero.moveDown();
                hero.setDirect(1);

                break;
            case KeyEvent.VK_LEFT:
            case KeyEvent.VK_A:

                hero.moveLeft();
                hero.setDirect(2);

                break;
            case KeyEvent.VK_RIGHT:
            case KeyEvent.VK_D:

                hero.moveRight();
                hero.setDirect(3);
                break;
        }

        // 发射子弹
        switch (e.getKeyCode()){
            case KeyEvent.VK_J:
                this.hero.shotEnemy();
//                heroShot = new HeroShot(hero.getX(), hero.getY());
//                hero.emitShot(heroShot);
//                heroShot.setDirect(hero.direct);
//                Thread thread = new Thread(heroShot);
//                thread.start();
                break;
        }
        this.repaint();
    }

    @Override
    public void keyReleased(KeyEvent e) {
//        System.out.println("31");
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(15);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
//            System.out.println(11111);
            repaint();
        }

    }
}

class Tank {

    int x = 0;
    int y = 0;
    int x2 = 0;
    int y2 = 0;
    int speed = 2;
    int direct = 0;
    int color;
    Boolean isLive = true;
    // 宽20，长30
    int sizeX = 20;
    int sizeY = 30;

    public Tank(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getDirect() {
        return direct;
    }

    public void setDirect(int direct) {
        this.direct = direct;
    }

    public int getSizeX() {
        return sizeX;
    }

    public void setSizeX(int sizeX) {
        this.sizeX = sizeX;
    }

    public int getSizeY() {
        return sizeY;
    }

    public void setSizeY(int sizeY) {
        this.sizeY = sizeY;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }

    public void moveUp() {
        this.y = this.y - this.speed;
    }

    public void moveDown() {
        this.y = this.y + this.speed;
    }

    public void moveLeft() {
        this.x = this.x - this.speed;
    }

    public void moveRight() {
        this.x = this.x + this.speed;
    }

    public Boolean getIsLive() {
        return isLive;
    }

    public void setIsLive(Boolean live) {
        isLive = live;
    }

    // 得到tank坐标x2
    public int getX2() {
        switch (direct) {
            case 0:
            case 1:
                x2 = x + sizeX;
                break;
            case 2:
            case 3:
                x2 = x + sizeY;
                break;
        }
        return x2;
    }

    public int getY2() {
        switch (direct) {
            case 0:
            case 1:
                y2 = y + sizeY;
            break;
            case 2:
            case 3:
                y2 = y + sizeX;
            break;
        }
        return y2;
    }


}

/**
 * 我的坦克
 */
class Hero extends Tank {
    HeroShot heroShot = null;
    Vector<HeroShot> heroShots = new Vector<HeroShot>();
    public Hero(int x, int y) {
        super(x, y);
        super.setSpeed(6);
    }

    // 发射子弹
    public void shotEnemy() {
        int shotX = 0;
        int shotY = 0;
        // 最多5发子弹
        if (this.heroShots.size() >= 5) return;
        switch (direct) {
            // 上
            case 0:
                shotX = x + 10;
                shotY = y;
                break;
            // 下
            case 1:
                shotX = x + 10;
                shotY = y + 30;
                break;
            // 左
            case 2:
                shotX = x;
                shotY = y + 10;
                break;
            // 右
            case 3:
                shotX = x + 30;
                shotY = y + 10;
                break;
        }
        heroShot = new HeroShot(shotX, shotY);
        heroShot.setDirect(direct);
        Thread thread = new Thread(heroShot);
        thread.start();
        heroShots.add(heroShot);
    }
}

/**
 * 敌人的坦克
 */
class EnemyTank extends Tank implements Runnable {
    // 坦克朝一个方向走的步数
    private int straightTimes = 5;
    // 坦克发出上一颗子弹到现在的时间
    private int lastShotTime = 0;
    Vector<EnemyShot>  enemyShots= new Vector<EnemyShot>();
    public EnemyTank(int x, int y) {
        super(x, y);
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(40);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            switch (direct) {
                // 上
                case 0:
                    y -= speed;
                    if (y < 0) {
                        y = 0;
                    }
                    break;
                // 下
                case 1:
                    y += speed;
                    if (y > 270) {
                        y = 270;
                    }
                    break;
                // 左
                case 2:
                    x -= speed;
                    if (x < 0) {
                        x = 0;
                    }
                    break;
                // 右
                case 3:
                    x += speed;
                    if (x > 370) {
                        x = 370;
                    }
                    break;
            }

            // 随机一个方向，随机步数
            if (this.straightTimes > 0 ){
                this.straightTimes--;
            } else {
                direct = (int) (Math.random() * 4);
                this.straightTimes = (int) (Math.random() * 15 + 3);
            }

            // 间隔1s，才1/3到概率去发射下一发子弹
            this.lastShotTime += 40;
            if (enemyShots.size() == 0) {
                if (((int) (Math.random() * 10)) < 1) {
                    this.lastShotTime = 0;
                    this.shotEnemy();
                }
            } else {
                if (this.lastShotTime % 1000 == 0) {
                    if (((int) (Math.random() * 3)) < 1) {
                        this.lastShotTime = 0;
                        this.shotEnemy();
                    }
                }
            }

            if (!isLive) {
                break;
            }
        }
    }

    // 发射子弹
    public void shotEnemy() {
        int shotX = 0;
        int shotY = 0;
        // 最多5发子弹
        if (this.enemyShots.size() >= 3) return;
        switch (direct) {
            // 上
            case 0:
                shotX = x + 10;
                shotY = y;
                break;
            // 下
            case 1:
                shotX = x + 10;
                shotY = y + 30;
                break;
            // 左
            case 2:
                shotX = x;
                shotY = y + 10;
                break;
            // 右
            case 3:
                shotX = x + 30;
                shotY = y + 10;
                break;
        }
        EnemyShot enemyShot = new EnemyShot(shotX, shotY);
        enemyShot.setDirect(direct);
        Thread thread = new Thread(enemyShot);
        thread.start();
        enemyShots.add(enemyShot);
    }
}



/**
 * 子弹
 */
class Shot implements Runnable {
    int x;
    int y;
    int direct;
    int color;
    int speed = 1;
    Boolean isLive = true;

    public Shot(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getDirect() {
        return direct;
    }

    public void setDirect(int direct) {
        this.direct = direct;
    }

    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public Boolean getIsLive() {
        return isLive;
    }

    public void setIsLive(Boolean isLive) {
        this.isLive = isLive;
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(15);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            switch (direct) {
                // 上
                case 0:
                    y -= speed;
                    break;
                // 下
                case 1:
                    y += speed;
                    break;
                // 左
                case 2:
                    x -= speed;
                    break;
                // 右
                case 3:
                    x += speed;
                    break;
            }
            // 子弹消失到边界
            if (x < 0 || x > 400 || y < 0 || y > 300) {
                this.isLive = false;
                break;
            }
//            System.out.println(x);
        }
    }
}

/**
 * 我的子弹
 */
class HeroShot extends Shot {
    public HeroShot(int x, int y) {
        super(x, y);
        super.setSpeed(1);
    }
}

/**
 * 敌方子弹
 */
class EnemyShot extends Shot {
    public EnemyShot(int x, int y) {
        super(x, y);
        super.setSpeed(1);
    }
}


/**
 * 炸弹
 */
class Bomb {
    int x, y;
    // 生命
    int life = 9;
    Boolean isLive = true;

    public Bomb(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getLife() {
        return life;
    }

    public void setLife(int life) {
        this.life = life;
    }

    public Boolean getLive() {
        return isLive;
    }

    public void setLive(Boolean live) {
        isLive = live;
    }

    // 减少生命
    public void lifeDown() {
        if (life > 0) {
            life--;
        } else {
            isLive = false;
        }
    }
}