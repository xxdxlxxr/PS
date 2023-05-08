import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int N = sc.nextInt();
	    int answer = 0;
	    
	    for (int i = 0; i < N; i++) {
	        String word = sc.next();
	        boolean arr[] = new boolean[26];
	        boolean tmp = true;
	        
	        for (int j = 0; j < word.length(); j++) {
	            int index = word.charAt(j) - 'a';
	            
	            if (arr[index]) {
	                if (word.charAt(j) != word.charAt(j - 1)) {
	                    tmp = false;
	                    break;
	                }
	            }
	            else arr[index] = true;
	        }
	        
	        if (tmp) answer++;
	    }
		
		System.out.println(answer);
	}
}