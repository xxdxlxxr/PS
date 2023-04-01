import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int H, M;
		H = sc.nextInt();
		M = sc.nextInt();
		
		M -= 45;
		
		if (M < 0) {
		    H -= 1;
		    M += 60;
		}
		
		if (H == -1) H = 23;
		
		System.out.print(H + " " + M);
	}
}