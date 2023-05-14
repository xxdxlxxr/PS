import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int A = sc.nextInt(), B = sc.nextInt(), V = sc.nextInt();
	    
		if ((V - A) % (A - B) == 0) System.out.println((V - A) / (A - B) + 1);
		else System.out.println((V - A) / (A - B) + 2);
	}
}