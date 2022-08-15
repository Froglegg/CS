#include <stdio.h>

void bubbleSort(int *A, int n, int (*compare)(int, int)) {
  int i, j, temp;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n - 1; j++) {
      // compare A[j] with A[j+1] and SWAP if needed
      if (A[j] > A[j + 1]) {
        temp = A[j];
        A[j] = A[j + 1];
        A[j + 1] = temp;
      }
    }
  }
}

int main(void) {
  int A[] = {3, 2, 1, 5, 6, 4};
  bubbleSort(A, 6);
  for (int i = 0; i < 6; i++) {
    printf("%d ", A[i]);
  }

  // what if sometimes you want to list desc or asc?

  return 0;
}