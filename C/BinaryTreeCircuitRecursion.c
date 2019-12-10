#include <stdio.h>

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

TreeNode* preorder(TreeNode *root) {
	if (root != NULL) {
		printf(" [%d] ", root->data);
		preorder(root->left);
		preorder(root->right);
	}
}

void 이진트리_재귀() {
	preorder(root);
}