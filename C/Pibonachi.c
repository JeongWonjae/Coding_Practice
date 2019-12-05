#include <stdio.h>

void pibonachi() {
	int i;
	int x = 0, y = 1;
	int aux = 0;

	printf("How many repeat?\n");
	scanf_s("%d", &i, sizeof(5));

	for (; i > 0; i--)
	{
		printf("%d", aux);
		aux = y;
		y = x + y;
		x = aux;
	}
	printf("\n");
}