//이진트리 레벨 순회
#include <stdio.h>

typedef struct {
	int data;
	struct TreeNode *left, *right;
}TreeNode;

typedef TreeNode *element;
#define MAX_SIZE 10
typedef struct {
	element data[MAX_SIZE];
	int front, rear;
}QueueType;

void init(QueueType *q) {
	q->front = q->rear = 0;
}

int is_full(QueueType *q) {
	return (q->rear+1)%MAX_SIZE==q->front;
}

int is_empty(QueueType *q) {
	return q->front == q->rear;
}

void enqueue(QueueType *q, element data) {
	if (is_full(q)) { return; }
	q->rear = (q->rear + 1) % MAX_SIZE;
	q->data[q->rear] = data;
}

element dequeue(QueueType *q) {
	if (is_empty(q)) { return NULL; }
	q->front = (q->front + 1) % MAX_SIZE;
	return q->data[q->front];
}

void level_order(TreeNode *root) {
	QueueType q;
	init(&q);

	if (root == NULL) { return; }
	enqueue(&q, root);
	while (!is_empty(&q)) {
		root = dequeue(&q);
		printf(" [%d] ", root->data);
		if (root->left) { enqueue(&q, root->left); }
		if (root->right) { enqueue(&q, root->right); }
	}
}

TreeNode n7 = { 7, NULL, NULL };
TreeNode n6 = { 6, NULL, NULL };
TreeNode n5 = { 5, NULL, NULL };
TreeNode n4 = { 4, NULL, NULL };
TreeNode n3 = { 3, &n6, &n7 };
TreeNode n2 = { 2, &n4, &n5 };
TreeNode n1 = { 1, &n2, &n3 };
TreeNode *root = &n1;

void 이진트리_순회_레벨() {
	level_order(root);
}