import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A, B, temp;
		A = sc.nextInt();
		B = sc.nextInt() + sc.nextInt();
		
		if (B >= 60) {
		    temp = B / 60;
		    A += temp;
		    B %= 60;
		    
		    if (A >= 24) A %= 24;
		}
		
		System.out.print(A + " " + B);
	}
}