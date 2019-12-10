#include <stdio.h>

typedef struct {
	int data;
	struct TreeNode *left, *right;
}TreeNode;

TreeNode n6 = { 6, NULL, NULL };
TreeNode n7 = { 7, NULL, NULL };
TreeNode n4 = { 4, NULL, NULL };
TreeNode n3 = { 3, &n6, &n7 };
TreeNode n2 = { 2, &n4, NULL };
TreeNode n1 = { 1, &n2, &n3 };
TreeNode *root = &n1;

int get_leaf_count(TreeNode *root) {
	int count=0;
	if (root) {
		if (root->left == NULL && root->right == NULL) {
			return 1;
		}
		count = get_leaf_count(root->left) + get_leaf_count(root->right);
	}
	return count;
}

void 단말노드개수() {
	printf("단말 노드의 개수는 %d입니다.", get_leaf_count(root));
}