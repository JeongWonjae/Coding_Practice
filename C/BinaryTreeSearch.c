#include <stdio.h>
#pragma warning(disable:4996)

typedef struct {
	int data;
	struct TreeNode *left, *right;
}TreeNode;

TreeNode n7 = { 70, NULL, NULL };
TreeNode n6 = { 55, NULL, NULL };
TreeNode n4 = { 20, NULL, NULL };
TreeNode n3 = { 65, &n6, &n7 };
TreeNode n2 = { 25, &n4, NULL };
TreeNode n1 = { 50, &n2, &n3 };
TreeNode *root = &n1;
TreeNode *tmp = &n1;

TreeNode* find_key(TreeNode *root, int key) {
	while (root != NULL) {
		if (root->data == key) { return root; }
		else if (root->data > key) { root = root->left; }
		else { root = root->right; }
	}
	return NULL;
}

TreeNode* find_key_re(TreeNode *root, int key) {
	if (root == NULL) { return NULL; }
	else if (root->data == key) { return root; }
	else if (root->data > key) { find_key_re(root->left, key); }
	else { find_key_re(root->right, key); }
}

void ����Ž��Ʈ��() {
	while (1) {
		int key;
		printf("ã�� �� �Է� >");
		scanf("%d", &key);
		tmp = find_key_re(root, key);
		if (tmp != NULL) {
			printf("%d���� ã�ҽ��ϴ�.\n", key);
		}
		else {
			printf("���� ã�� ���Ͽ����ϴ�.\n");
		}
	}
}