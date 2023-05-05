import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    String s = sc.next();
	    int max = 0;
	    int[] arr = new int[26];
	    char answer = '?';
	    
	    for (int i = 0; i < s.length(); i++) {
	        if (s.charAt(i) >= 'a') arr[s.charAt(i) - 'a']++;
	        else arr[s.charAt(i) - 'A']++;
	    }
	    
	    for (int i = 0; i < 26; i++) {
	        if (arr[i] == max) answer = '?';
	        else if (arr[i] > max) {
	            max = arr[i];
	            answer = (char) ('A' + i);
	        }
	    }
	    
		System.out.print(answer);
	}
}