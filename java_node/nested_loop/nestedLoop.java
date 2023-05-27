package nested_loop;

public class nestedLoop {
    public static void main(String[] args) {
        boolean flag = false;
        int counter = 0;
        for (int i=1;i<201;i++){
            flag = isPrime(i);
            if(flag == true){
                System.out.println(i);
                counter += 1;
            }
        }
        System.out.print(counter);
        System.out.println(" prime numbers");
    }
    static boolean isPrime(int n){
        boolean flag = true;
        int j = 0;
        for (j = 2; j<n;j++){
            if(n % j==0){
                flag = false;
                break;
            }
        }
        return flag;
    }
    
}
