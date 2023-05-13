import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int X = sc.nextInt(), i = 1, sum = 0;
	    
	    while (X > sum) {
            sum += i;
            i += 1;
        }
        
        if (i % 2 == 0) System.out.println(sum - X + 1 + "/" + (X - sum + i - 1));
        else System.out.print(X - sum + i - 1 + "/" + (sum - X + 1));
	}
}