import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    String input = sc.nextLine();
	    int cnt = 0;
	    
	    for (int i = 0; i < input.length(); i++) {
	        if (input.charAt(i) >= 65 & input.charAt(i) <= 67) cnt += 3;
	        else if (input.charAt(i) >= 68 & input.charAt(i) <= 70) cnt += 4;
            else if (input.charAt(i) >= 71 & input.charAt(i) <= 73) cnt += 5;
            else if (input.charAt(i) >= 74 & input.charAt(i) <= 76) cnt += 6;
            else if (input.charAt(i) >= 77 & input.charAt(i) <= 79) cnt += 7;
            else if (input.charAt(i) >= 80 & input.charAt(i) <= 83) cnt += 8;
            else if (input.charAt(i) >= 84 & input.charAt(i) <= 86) cnt += 9;
            else cnt += 10;
	    }
	    
		System.out.println(cnt);
	}
}