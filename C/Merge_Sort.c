#include <stdio.h>

int merge_sort() {
	int A[5] = {13, 14, 15, 17, 19};
	int B[5] = {10, 12, 13, 17, 18};
	int C[10];
	int i = 0;
	int j = 0;
	int k = 0;
	int n = sizeof(A) / sizeof(A[0]);
	int m = sizeof(B) / sizeof(B[0]);

	for (int z = 0; z < 10; z++) {
		if (A[i] <= B[j]) {
			C[k] = A[i];
			i = i + 1;
			k = k + 1;
			if (i >= n) {
				for (int num = j; num < m; num++) {
					C[k] = B[num];
					k = k + 1;
				}
				break;
			}
		}
		if (A[i] >= B[j]) {
			C[k] = B[j];
			j = j + 1;
			k = k + 1;
			if (j >= n) {
				for (int num = i; num < n; num++) {
					C[k] = A[num];
					k = k + 1;
				}
				break;
			}
		}
	}

	for (int u = 0; u < 10; u++) {
		printf("%d ", C[u]);
	}
}