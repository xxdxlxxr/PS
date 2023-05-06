import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int C = sc.nextInt();
	    
	    for (int i = 0; i < C; i++){
	        int N = sc.nextInt();
	        int[] scores = new int[N];
	        int sum = 0;
	        double cnt = 0;
	        
	        for (int j = 0; j < N; j++) {
	            int score = sc.nextInt();
	            scores[j] = score;
	            sum += score;
	        }
	        
	        double avg = (sum / N);
	        
	        for (int j = 0; j < N; j++) if (scores[j] > avg) cnt++;
	        
	        System.out.printf("%.3f%%\n", 100 * cnt / N);
	    }
	}
}