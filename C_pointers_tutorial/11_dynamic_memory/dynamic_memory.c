#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a; // goes on stack
  int *p;
  // create a block on the heap to store an integer
  p = (int *)malloc(sizeof(int));
  // only way to use data on the heap is through dereferencing
  // assign a value to by dereferencing the pointer and assigning a value
  *p = 10;
  // free allocated memory, very important
  free(p);
  // good practice to set p to NULL to prevent future issues
  p = NULL;
  // allocate a block for an array of 20 integers on the heap
  p = (int *)malloc(20 * sizeof(int));
  // we can then treat p as an array
  p[0] = 1;
  p[1] = 2;
  p[2] = 3;
  p[3] = 4;
  // etc...

  return 0;
}