#include <stdio.h>
// callback function should compare two integers, and return 1 if first relement has
// higher rank, 0 if elements are equal, and -1 if second element has higher rank
void bubbleSort(int *A, int n, int (*callback_function_compare)(int, int)) {
  int i, j, temp;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n - 1; j++) {
      // compare A[j] with A[j+1] and SWAP if needed
      if (callback_function_compare(A[j], A[j + 1]) > 0) {
        temp = A[j];
        A[j] = A[j + 1];
        A[j + 1] = temp;
      }
    }
  }
}

int callback_function_compare(int a, int b) { return a > b ? 1 : -1; }

int main(void) {
  int A[] = {3, 2, 1, 5, 6, 4};
  bubbleSort(A, 6, callback_function_compare);
  for (int i = 0; i < 6; i++) {
    printf("%d ", A[i]);
  }

  // what if sometimes you want to list desc or asc?

  return 0;
}