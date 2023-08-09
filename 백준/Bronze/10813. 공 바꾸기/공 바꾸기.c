#include <stdio.h>

int main()
{
	int N, M, i, j, tmp;
	scanf("%d %d", &N, &M);
	int nums[100];

	for (int i = 0; i < 100; i++) nums[i] = i + 1;

	for (int l = 0; l < M; l++) {
		scanf("%d %d", &i, &j);

		tmp = nums[i - 1];
		nums[i - 1] = nums[j - 1];
		nums[j - 1] = tmp;
	}

	for (int n = 0; n < N; n++) printf("%d ", nums[n]);
}