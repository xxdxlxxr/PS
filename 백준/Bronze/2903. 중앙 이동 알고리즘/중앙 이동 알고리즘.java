import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int N = sc.nextInt();
	    int answer = 1;
	    
	    for (int i = 0; i < N; i++) answer *= 2;
	    
		System.out.println((answer + 1) * (answer + 1));
	}
}