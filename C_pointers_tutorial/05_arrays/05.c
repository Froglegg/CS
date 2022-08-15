#include <stdio.h>

int main(void) {
  int A[] = {2, 4, 5, 8, 1};
  //   // print address of first element array
  //   printf("%p\n", A);
  //   // also print address of first element in array
  //   printf("%p\n", &A[0]);
  //   // print first element in array
  //   printf("%d\n", A[0]);
  //   // this will also print first element in array
  //   printf("%d\n", *A);

  // arrays are pointers
  int *p = A;
  for (int i = 0; i < 5; i++) {

    printf("Address of %d is %p\n", i, &A[i]);
    printf("Address of %d is %p\n", i, A + i);
    printf("value = %d\n", A[i]);
    printf("value = %d\n", *(A + i));
  }

  return 0;
}