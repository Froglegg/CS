#include <stdio.h>

// we could pass int *A or int A[], it's the same
// this is because the compiler always does a call by reference for arrays
// and creates a pointer to the base element of the array
int sumOfElements(int *A, int size) {
  int i, sum = 0;
  for (i = 0; i < size; i++) {
    sum += A[i];
  }

  return sum;
}

// we can modify elements of an array in place by dereferencing them in the callee
void Double(int A[], int size) {
  for (int i = 0; i < size; i++) {
    A[i] = 2 * A[i];
  }
}

int main(void) {
  int A[] = {1, 2, 3, 4, 5};
  // divide size of Array by size of integers to get number of elements
  // this step actually needs to take place in the caller, because arrays are always
  // called by reference in callee functions
  int size = sizeof(A) / sizeof(A[0]);
  // we could pass A or &A[0], as it's the same thing!
  int total = sumOfElements(A, size);
  int total_2 = sumOfElements(&A[0], size);
  printf("%d\n", total);
  printf("%d\n", total_2);

  // we can modify elements in an array by dereferencing them in the callee
  Double(A, size);
  // this will return 2, 4, 6, 8, 10
  for (int i = 0; i < size; i++) {
    printf("%d\n", A[i]);
  }
  return 0;
}