#include <stdio.h>

typedef struct {
	int data;
	struct TreeNode *left, *right;
}TreeNode;

TreeNode n7 = { 7, NULL, NULL };
TreeNode n6 = { 6, NULL, NULL };
TreeNode n5 = { 5, NULL, NULL };
TreeNode n4 = { 4, NULL, NULL };
TreeNode n3 = { "+", &n6, &n7 };
TreeNode n2 = { "-", &n4, &n5 };
TreeNode n1 = { "*", &n2, &n3 };
TreeNode *root = &n1;

int eval(TreeNode *root) {
	if (root == NULL) { return; }
	else if(root->right == NULL && root->left == NULL) return root->data;
	else {
		int op1 = eval(root->left);
		int op2 = eval(root->right);
		printf(" %d %s %d 를 계산합니다.\n", op1, root->data, op2);
		if (root->data == "+") return op1 + op2;
		else if (root->data == "-") return op1 - op2;
		else if (root->data == "*") return op1 * op2;
	}
	return 0;
}

void 이진트리_수식계산() {
	printf("수식 값읠 결과는 %d입니다.", eval(root));
}