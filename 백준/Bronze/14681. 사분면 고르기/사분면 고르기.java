import java.util.*;
import java.lang.Math;

public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int x, y;
		int [][] arr = {{3, 2}, {4, 1}};
		
		x = sc.nextInt();
		y = sc.nextInt();
		
		x = (x / Math.abs(x) + 1) / 2;
        y = (y / Math.abs(y) + 1) / 2;
		
		System.out.println(arr[x][y]);
	}
}