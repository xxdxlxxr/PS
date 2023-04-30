import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int A = sc.nextInt();
	    int B = sc.nextInt();
	    
	    A = A / 100 + ((A / 10) % 10) * 10 + ((A % 100) % 10) * 100;
        B = B / 100 + ((B / 10) % 10) * 10 + ((B % 100) % 10) * 100;
	    
		if (A > B) System.out.println(A);
		else System.out.println(B);
	}
}