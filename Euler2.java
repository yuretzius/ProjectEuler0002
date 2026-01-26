import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Euler2 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        long a, b, temp;
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextLong();
            a = 0;
            b = 2;
            while (b<=n){
               temp = a + 4*b; // see the README
               a = b;
               b = temp;
            } 
            // see the README
            System.out.println((b+a-2)/4); 
        }
    }
}
