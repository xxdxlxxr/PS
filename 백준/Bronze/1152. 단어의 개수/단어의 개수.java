import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    String s = sc.nextLine();
	    String answer[] = s.trim().split(" ");
	    
	    if (answer.length == 1 & answer[0] == "") System.out.println(0);
	    else System.out.println(answer.length);
	}
}