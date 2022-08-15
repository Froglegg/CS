#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int n;
  printf("Enter size of array:\n");
  scanf("%d", &n);

  // can use malloc or calloc here
  // calloc fills values in with zero for each byte
  //   int *A = malloc(n * sizeof(int));
  int *A = calloc(n, sizeof(int));

  for (int i = 0; i < n; i++) {
    A[i] = i + 1;
  }

  for (int i = 0; i < n; i++) {
    printf("%d ", A[i]);
  }
  // if size of new block > previous block, and it is possible to extend the previous
  // block, it is extended, else, a new block is created
  int *B = (int *)realloc(A, 2 * n * sizeof(int));
  // A is released after realloc, no need to free A
  //   free(A);
  // free B instead
  free(B);
  A = NULL;
  B = NULL;
  return 0;
}