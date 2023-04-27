import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int[] arr = new int[26];
	    
	    for (int i = 0; i < arr.length; i++) arr[i] = -1;
	    
	    String s = sc.next();
	    
	    for (int i = 0; i < s.length(); i++) {
	        char alpha = s.charAt(i);
	        
	        if (arr[alpha - 'a'] == -1) arr[alpha - 'a'] = i;
	    }
	    
	    for (int val:arr) System.out.print(val + " ");
	}
}