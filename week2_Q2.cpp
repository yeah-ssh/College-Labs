#include <stdio.h>

#define MAX 10

void transpose(int matrix[MAX][MAX], int trans[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            trans[j][i] = matrix[i][j];
        }
    }
}

int main() {
    int matrix[MAX][MAX], trans[MAX][MAX], row, col;

    printf("Enter rows and columns of matrix: ");
    scanf("%d %d", &row, &col);

    printf("Enter elements of matrix:\n");
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            scanf("%d", &matrix[i][j]);
        }
    }

    transpose(matrix, trans, row, col);

    printf("\nTranspose of Matrix:\n");
    for (int i = 0; i < col; ++i) {
        for (int j = 0; j < row; ++j) {
            printf("%d ", trans[i][j]);
        }
        printf("\n");
    }

    return 0;
}
