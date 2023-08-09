#include <stdio.h>

int main()
{
	int N, M, i, j, k;
	scanf("%d %d", &N, &M);
	int nums[100] = { 0 };

	for (int l = 0; l < M; l++) {
		scanf("%d %d %d", &i, &j, &k);

		for (int m = i; m <= j; m++) nums[m - 1] = k;
	}

	for (int n = 0; n < N; n++) printf("%d ", nums[n]);
}