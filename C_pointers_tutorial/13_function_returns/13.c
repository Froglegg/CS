#include <stdio.h>
#include <stdlib.h>

// called function (callee)
int AddByValue(int a, int b) {
  // a and b are different memory addresses as Add is in a different stack frame than
  // Main
  int c = a + b;
  return c;
}
// returns poitner to integer
int *AddByReference(int *a, int *b) {
  int c = *a + *b;
  return &c;
}

// calling function (caller)
int main(void) {

  static int a = 2, b = 4;
  // Add is here called by value
  int c = AddByValue(a, b);
  // lets call it by reference
  int *c2 = AddByReference(&a, &b);
  // this should print out the correct value
  printf("Sum of call by value = %d\n", c);
  // this prints out some garbage, BUT ONlY if you call a function before the call by
  // reference function, which returns a pointer
  // this is because between allocating memory space for the initialized variables a and
  // b and call by reference, the space if deallocated, and so while you are returning a
  // memory address, it may no longer exist

  printf("Sum of call by reference = %d\n", *c2);
  return 0;
}