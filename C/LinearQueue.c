#include <stdio.h>
#define MAX_QUEUE_SIZE 5

typedef int element;
typedef struct {
	element queue[MAX_QUEUE_SIZE];
	int front;
	int rear;
}QueueType;

void init(QueueType *q) {
	q->front = q->rear = -1;
	for (int i = 0; i < MAX_QUEUE_SIZE; i++) {
		q->queue[i] = NULL;
	}
}

int is_empty(QueueType *q) {
	return (q->front == q->rear);
}

int is_full(QueueType *q) {
	return (q->rear >= MAX_QUEUE_SIZE-1);
}

void enqueue(QueueType *q, element value) {
	if (is_full(q)) { printf("큐가 가득찬 상태\n"); }
	else {
		q->queue[++(q->rear)] = value;
	}
}

int dequeue(QueueType *q) {
	if (is_empty(q)) { printf("큐가 공백인 상태\n"); }
	else {
		q->queue[++(q->front)] = NULL; 
		return q->queue[q->front];
	}
}

void lookup(QueueType *q) {
	printf("Queue front=%d rear=%d : ", q->front, q->rear);
	for (int i = 0; i < MAX_QUEUE_SIZE; i++) {
		if (i <= q->front && i > q->rear) {
			printf(" | ");
		}
		else {
			printf(" %d | ", q->queue[i]);
		}
	}
	printf("\n");
}

void 선형_큐() {
	QueueType q;
	init(&q);

	enqueue(&q, 10); lookup(&q);
	enqueue(&q, 20); lookup(&q);
	enqueue(&q, 30); lookup(&q);
	enqueue(&q, 40); lookup(&q);
	enqueue(&q, 50); lookup(&q);
	enqueue(&q, 60); lookup(&q);

	dequeue(&q); lookup(&q);
	dequeue(&q); lookup(&q);
	dequeue(&q); lookup(&q);
	dequeue(&q); lookup(&q);
	dequeue(&q); lookup(&q);
	dequeue(&q); lookup(&q);
}