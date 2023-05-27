package Loop;

public class Falling {
    public static void main(String[] args) {
        running();
    }
    static void running(){
        double s = 100;//total instance
        double height = 100;
        int n = 10;
        double  d =0;
        for(int i =1;i<= n;i++){
            s += d;
            height /= 2;
            d = height * 2;
        }
        System.out.println("total:"+s);
        System.out.println("height:"+height);

    }
}
