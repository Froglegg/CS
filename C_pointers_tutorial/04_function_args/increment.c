#include <stdio.h>

// call by value
void increment(int a) {

  a = a + 1;
  printf("address of a in increment function is: %p\n", &a);
}
// call by reference
void increment_pointer(int *p) { *p = (*p) + 1; }

int main(void) {
  int a = 10;
  increment(a);
  // address will be different in main and increment
  printf("address of a in main function is: %p\n", &a);
  // value will not be changed
  printf("value of a is: %d\n", a);
  // if we pass an address instead, we can incremenet the variable
  increment_pointer(&a);
  // value will be
  printf("value of a is: %d\n", a);
  return 0;
}