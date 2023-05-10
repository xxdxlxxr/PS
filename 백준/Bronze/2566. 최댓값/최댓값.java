import java.util.*;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int nums[][] = new int[9][9];
	    int answer = 0, row = 0, col = 0;
	    
	    for (int i = 0; i < 9; i++) {
	        for (int j = 0; j < 9; j++) {
	            nums[i][j] = sc.nextInt();
	            
	            if (nums[i][j] > answer) {
	                answer = nums[i][j];
	                row = i;
	                col = j;
	            }
	        }
	    }
	    
		System.out.println(answer);
		System.out.println((row + 1) + " " + (col + 1));
	}
}