import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int A, B;
	    
	    while (true) {
	        A = sc.nextInt();
	        B = sc.nextInt();
	        
	        if (A == 0) break;
	        
	        System.out.println(A + B);
	    }
	}
}