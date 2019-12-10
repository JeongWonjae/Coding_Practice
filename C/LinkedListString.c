#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable: 4996)

typedef struct {
	char name[100];
}element;

typedef struct {
	element data;
	struct ListNode *link;
}ListNode;

ListNode* insert_first(ListNode *head, element value) {
	ListNode *p = (ListNode*)malloc(sizeof(ListNode));
	if (p != NULL) {
		p->data = value;
		p->link = head;
		head = p;
		return head;
	}
}

ListNode* search_for(ListNode *head, element value) {
	ListNode *p;
	for (p = head; p != NULL; p = p->link) {
		if (strcmp(p->data.name, value.name) == 0) {
			return p;
		}
	}
	return NULL;
}

ListNode* search_while(ListNode *head, element value) {
	ListNode *p = head;
	while (p != NULL) {
		if (strcmp(p->data.name, value.name) == 0) { return p; }
		p = p->link;
	}
	return NULL;
}

void lookup(ListNode *head) {
	ListNode *p;
	for (p = head; p != NULL; p = p->link) {
		printf(" %s -> ", p->data.name); //check
	}
	printf(" NULL \n");
}

ListNode* concat(ListNode *head1, ListNode *head2) {
	if (head1 == NULL) return head2;
	else if (head2 == NULL) return head1;
	else {
		ListNode *p = head1;
		while (p->link != NULL) {
			p = p->link;
		}
		p->link = head2;
		return head1;
	}
}

void ���ڿ�_����_����Ʈ() {
	ListNode *head = NULL;
	element data; //check

	strcpy(data.name, "WONJAE"); //check
	head = insert_first(head, data);
	lookup(head);

	strcpy(data.name, "SANGBIN"); //check
	head = insert_first(head, data);
	lookup(head);

	strcpy(data.name, "ABCDEFG"); //check
	head = insert_first(head, data);
	lookup(head);

	strcpy(data.name, "WONJAE");
	if (search_for(head, data) != NULL) {
		printf("%s�� �����մϴ�.\n", data.name);
	}
	else {
		printf("�������� �ʽ��ϴ�\n.");
	}

	strcpy(data.name, "AAA");
	if (search_while(head, data) != NULL) {
		printf("%s�� �����մϴ�.\n", data.name);
	}
	else {
		printf("�������� �ʽ��ϴ�.\n");
	}
	ListNode *head2 = NULL;

	strcpy(data.name, "BANANA"); //check
	head2 = insert_first(head2, data);
	lookup(head2);

	strcpy(data.name, "ORNAGE"); //check
	head2 = insert_first(head2, data);
	lookup(head2);

	printf("\n------�� ����Ʈ ��ġ��------\n");
	printf("����Ʈ 1 : "); lookup(head);
	printf("����Ʈ 2 : "); lookup(head2);

	ListNode *head3 = NULL;
	head3 = concat(head, head2);
	printf("����Ʈ 3 : "); lookup(head3);
}