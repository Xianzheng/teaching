public class reverseString {
    public static void main(String[] args) {
        char[] a = { 'a', 'b', 'c', 'd' };
        reverse(a, 0, a.length - 1);
        for (char i : a) {
            System.out.println(i);
        }
    }

    static void reverse(char[] temp, int start, int end) {
        if (temp == null) {
            return;
        }

        int k = temp.length;
        if (k % 2 == 0) {
            if (start == end + 1)
                return;
            // System.out.println(start + " " + end);
            char t = temp[start];
            temp[start] = temp[end];
            temp[end] = t;
            reverse(temp, start += 1, end -= 1);
        } else {

            if (start == end)
                return;

            char t = temp[start];
            temp[start] = temp[end];
            temp[end] = t;
            reverse(temp, start += 1, end -= 1);
        }

    }
}
