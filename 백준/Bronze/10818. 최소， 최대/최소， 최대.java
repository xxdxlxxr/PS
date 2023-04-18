import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int N = sc.nextInt();
	    int min = sc.nextInt();
	    int max = min;
	    
	    for (int i = 1; i < N; i++) {
	        int tmp = sc.nextInt();
	        
	        if (max < tmp) max = tmp;
	        if (min > tmp) min = tmp;
	    }
	    
		System.out.printf("%d %d", min, max);
	}
}