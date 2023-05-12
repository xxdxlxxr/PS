import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int N = sc.nextInt();
	    int tmp = 1, answer = 1;
	    
	    while (tmp < N) {
	        tmp += 6 * answer;
	        answer += 1;
	    }
	    
		System.out.println(answer);
	}
}