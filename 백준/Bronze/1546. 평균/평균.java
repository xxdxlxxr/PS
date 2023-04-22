import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int N = sc.nextInt();
	    int score, max = 0;
	    int sum = 0;
	    
	    for (int i = 0; i < N; i++) {
	        score = sc.nextInt();
	        sum += score;
	        
	        if (score > max) max = score;
	    }
	    
		System.out.println(100.0 * sum / max / N);
	}
}