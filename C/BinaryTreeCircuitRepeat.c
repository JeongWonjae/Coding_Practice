#include <stdio.h>
#define MAX_SIZE 10

typedef struct {
	int data;
	struct TreeNode *left, *right;
}TreeNode;

TreeNode n7 = { 7, NULL, NULL };
TreeNode n6 = { 6, NULL, NULL };
TreeNode n5 = { 5, NULL, NULL };
TreeNode n4 = { 4, NULL, NULL };
TreeNode n3 = { 3, &n6, &n7 };
TreeNode n2 = { 2, &n4, &n5 };
TreeNode n1 = { 1, &n2, &n3 };
TreeNode *root = &n1;

TreeNode *stack[MAX_SIZE];
int top = -1;

void push(TreeNode *node) {
	if (top < MAX_SIZE - 1) {
		stack[++top] = node;
	}
}

TreeNode *pop() {
	if (top >= 0) {
		return stack[top--];
	}
	return NULL;
}

void inorder_iter(TreeNode *root) {
	if (root != NULL) {
		while (1) {
			for (root; root != NULL; root = root->left) {
				push(root);
			}
			root = pop(root);
			if (root == NULL) { break; }
			printf(" [%d] ", root->data);
			root = root->right;
		}
	}
}

void 이진트리_순회반복() {
	inorder_iter(root);
}