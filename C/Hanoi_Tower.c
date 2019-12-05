#include <stdio.h>

void hanoi(int n, char a, char b, char c) {
	if (n == 1) {
		printf("[원판1] %s -> %s\n", a, c);
	}
	else {
		hanoi(n - 1, a, c, b);
		printf("[원판%d] %s -> %s\n", n, a, c);
		hanoi(n - 1, b, a, c);
	}
}