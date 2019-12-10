#include <stdio.h>

typedef struct{
	int exof, expon;
	struct ListNode *link;
}ListNode;

typedef struct {
	int size;
	ListNode *head;
	ListNode *tail;
}ListType;

ListType* create() {
	ListType *plist=(ListType*)malloc(sizeof(ListType));
	plist->size = 0;
	plist->head = plist->tail = NULL;
	return plist;
}

void insert_last(ListType *plist, int exof, int expon) {
	ListNode *tmp=(ListNode*)malloc(sizeof(ListNode));
	tmp->exof = exof;
	tmp->expon = expon;
	tmp->link = NULL;
	if (plist->tail == NULL) {
		plist->head = plist->tail = tmp;
	}
	else {
		plist->tail->link = tmp;
		plist->tail = tmp;
	}
	plist->size++;
}

void poly_add(ListType *plist1, ListType *plist2, ListType *plist3) {
	ListNode *a = plist1->head;
	ListNode *b = plist2->head;
	int sum=0;

	while (a&&b) {
		if (a->expon == b->expon) {
			sum = a->exof + b->exof;
			if (sum!=0) { insert_last(plist3, sum, a->expon); }
			a = a->link; b = b->link;
		}
		else if (a->expon > b->expon) {
			insert_last(plist3, a->exof, a->expon);
			a = a->link;
		}
		else {
			insert_last(plist3, b->exof, b->expon);
			b = b->link;
		}
	}

	for (; a; a = a->link) {
		insert_last(plist3, a->exof, a->expon);
	}
	for (; b; b = b->link) {
		insert_last(plist3, b->exof, b->expon);
	}
}

void print_list(ListType *plist) {
	ListNode *p = plist->head;
	for (p; p != NULL; p = p->link) {
		printf(" %d ^ %d -> ", p->exof, p->expon);
	}
	printf("\n");
}

void 리스트_다항식() {
	ListType *plist1 = create();
	ListType *plist2 = create();
	ListType *plist3 = create();

	insert_last(plist1, 5, 3);
	insert_last(plist1, 3, 2);
	insert_last(plist1, 2, 1);

	insert_last(plist2, 4, 4);
	insert_last(plist2, 4, 2);
	insert_last(plist2, 3, 1);
	insert_last(plist2, 1, 0);

	print_list(plist1);
	print_list(plist2);

	poly_add(plist1, plist2, plist3);
	print_list(plist3);
}