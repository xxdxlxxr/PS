import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int M = sc.nextInt(), N = sc.nextInt(), sum = 0, minimum = 0;
	    
	    for (int i = M; i <= N; i++) {
            for (int j = 2; j <= i; j++) {
                if (i % j == 0) break;
                
                if (j == i - 1) {
                    if (sum == 0) minimum = i;
                    
                    sum += i;
                }
            }
            
            if (i == 2) {
                sum += i;
                minimum = i;
            }
        }
        
        if (minimum == 0) System.out.println(-1);
        else {
            System.out.println(sum);
            System.out.println(minimum);
        }
	}
}