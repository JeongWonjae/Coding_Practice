#include <stdio.h>
#include <string.h>

typedef struct _information {
	char firstName[20];
	char lastName[20];
	int birth;
} information;

void typedeffunc() {
	information i1;
	information i2;

	strcpy(i1.firstName, "Jeong");
	strcpy(i1.lastName, "Wonjae");
	i1.birth = 950220;

	strcpy(i2.firstName, "Park");
	strcpy(i2.lastName, "Sangbin");
	i2.birth = 950209;

	printf("%d, %s %s\n", i1.birth, i1.firstName, i1.lastName);
	printf("%d, %s %s\n", i2.birth, i2.firstName, i2.lastName);

	return 0;
}


void typedeffunc2() {
	typedef int MYINT;
	typedef int* PMYINT;

	MYINT num;
	PMYINT numPtr;

	numPtr = &num; //변수의 주소가 저장됨
	printf("%d\n", numPtr);
	printf(num);
}