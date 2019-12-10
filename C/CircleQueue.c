#include <stdio.h>
#define MAX_QUEUE_SIZE 100

typedef struct {
	int data[MAX_QUEUE_SIZE];
	int rear, front;
}QueueType;

void init(QueueType *q) { q->front = q->rear = 0; }
int is_empty(QueueType *q) { return q->rear == q->front; }
int is_full(QueueType *q) { return (q->rear + 1) % MAX_QUEUE_SIZE == q->front; }

void enqueue(QueueType *q, int item) {
	if (is_full(q)) return;
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->data[q->rear] = item;
}

int dequeue(QueueType *q) {
	if (is_empty(q)) return;
	q->front = (q->front + 1) % MAX_QUEUE_SIZE;
	return q->data[q->front];
}

void print_queue(QueueType *q) {
	if (is_empty(q)) return;
	int i = q->front;
	do {
		i = (i + 1) % MAX_QUEUE_SIZE;
		printf(" %d || ", q->data[i]);
		if (i == q->rear) break;
	} while (i != q->front);
	printf("\n");
}

int fibonachi(QueueType *q, int repeat) {
	if (repeat == 0) return 0;
	if (repeat == 1) return 1;
	int op1; int op2; int res;
	enqueue(&q, 0); enqueue(&q, 1);
	for (int i = 2; i <= repeat; i++) {
		op1 = dequeue(&q);
		op2 = dequeue(&q);
		res = op1 + op2;
		enqueue(&q, op2);
		enqueue(&q, res);
	}
	res = dequeue(&q);
	res = dequeue(&q);
	return res;

}

void 원형큐() {
	QueueType q;
	init(&q);
	printf("피보나치의 결과는 %d", fibonachi(&q, 6));
}