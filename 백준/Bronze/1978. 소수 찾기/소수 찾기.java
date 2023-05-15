import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int N = sc.nextInt(), num, answer = 0;
	    
	    for (int i = 0; i < N; i++) {
            num = sc.nextInt();
        
            for (int j = 2; j <= num; j++) {
                if (num == j) answer++;
                
                if (num % j == 0) break;
            }
        }
        
		System.out.println(answer);
	}
}