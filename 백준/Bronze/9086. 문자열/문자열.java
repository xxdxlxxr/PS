import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int T = sc.nextInt();
	    
	    for (int i = 0; i < T; i++) {
	        String str = sc.next();
	        int len = str.length();
	        String first = String.valueOf(str.charAt(0));
	        String last = String.valueOf(str.charAt(len - 1));
	        
	        System.out.println(first + last);
	    }
	}
}