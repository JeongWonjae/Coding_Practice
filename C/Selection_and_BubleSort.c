#include <stdio.h>

void selective_sort() {
	int arr[9] = { 15, 17, 14, 20, 10, 13, 16, 1, 111 };
	int tmp;
	int arr_size = sizeof(arr)/sizeof(arr[0]);
	printf("%d\n", arr_size);
	for (int i = 0; i < arr_size-1; i++) {
		for (int j = i+1; j < arr_size; j++) {
			if (arr[i] > arr[j]) {
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
		for (int k = 0; k < arr_size; k++) {
			printf("%d ", arr[k]);
		}
		printf("\n");
	}
	printf("ÃÖÁ¾\n");
	for (int i = 0; i < arr_size; i++) {
		printf("%d ", arr[i]);
	}
}

void buble_sort() {
	int arr[5] = {1, 3, 5, 2, 4};
	int arr_size = sizeof(arr) / sizeof(arr[0]);

	for (int i= 0; i < arr_size-1; i++) {
		if (arr[i] > arr[i + 1]) {
			int tmp = arr[i + 1];
			arr[i + 1] = arr[i];
			arr[i] = tmp;
			printf("[switch %d]%d [i+1]%d\n",i , arr[i], arr[i + 1]);
		}
	}

	for (int i = 0; i < arr_size - 1; i++) {
		if (arr[i] > arr[i + 1]) {
			int tmp = arr[i + 1];
			arr[i + 1] = arr[i];
			arr[i] = tmp;
			printf("[switch %d]%d [i+1]%d\n", i, arr[i], arr[i + 1]);
		}
	}

	for (int j = 0; j < arr_size; j++) {
		printf("%d ", arr[j]);
	}
}

void 

