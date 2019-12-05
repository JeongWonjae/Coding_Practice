#include <stdio.h>

void hanoi(int n, char a, char b, char c) {
	if (n == 1) {
		printf("[����1] %s -> %s\n", a, c);
	}
	else {
		hanoi(n - 1, a, c, b);
		printf("[����%d] %s -> %s\n", n, a, c);
		hanoi(n - 1, b, a, c);
	}
}