public class hw35 {
    public static void main(String[] args) {
        
        System.out.println(palindrome("ABCBA", 0));
    }
    //hw:
        //find a string and seee if it is a palindrome
        //"abcba" is a palindrome, use recursive
        //redo the bbinarysearchteacher (i already did it it is binary search) and then add comments to ur code explaining it
    static boolean palindrome(String str,int index){
        if(str.charAt(index)==str.charAt(str.length()/2)){
            return true;
        }else{
            if(str.charAt(index)==str.charAt(str.length() -(index+1))){
                return palindrome(str, index+1);
            }else{
                return false;
            }
            
        }
        
        
    }
    static int binarySearch(int[] array,int start, int end,int key){
        
        if(start==end && array[start]!=key){
            return -1;
        }else{
            if (array[start]==key){
                return start;
            }else{
            return binarySearch(array, start+1, end, key);
            }
        }
        //use ur own code to do binary search to search for the num
    }
}
