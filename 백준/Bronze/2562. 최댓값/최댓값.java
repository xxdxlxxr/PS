import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int max = 0;
		int n, index = 0;
		
		for (int i = 0; i < 9; i++) {
		    n = sc.nextInt();
		    
		    if (max < n) {
		        max = n;
		        index = i + 1;
		    }
		}
		
		System.out.println(max);
		System.out.println(index);
	}
}