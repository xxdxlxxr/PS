import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n, answer = 0;
		int[] arr = new int[10];
		
		for (int i = 0; i < 10; i++) arr[i] = sc.nextInt() % 42;
		
		for (int i = 0; i < 10; i++) {
		    int cnt = 0;
		    
		    for (int j = i + 1; j < 10; j++) {
		        if (arr[i] == arr[j]) {
		            cnt++;
		            break;
		        }
		    }
		    
		    if (cnt == 0) answer++;
		}
		
		System.out.println(answer);
	}
}