import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int x = sc.nextInt(), y = sc.nextInt(), w = sc.nextInt(), h = sc.nextInt(), answer = x;
        
        if (answer > w - x) answer = w - x;
        if (answer > y) answer = y;
        if (answer > h - y) answer = h - y;
	    
		System.out.println(answer);
	}
}