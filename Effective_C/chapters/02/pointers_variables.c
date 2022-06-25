#include <stdio.h>
// declare pointers within definition using the indirection operator *
// when used in a finction declaration, * acts as part of a pointer delcarator
// indicating that the parameter is a pointer to an object or function
void swap(int *pa, int *pb) {
  // when used in expressions within a function, the unary operator * dereferences the
  // pointer to the object,
  int t = *pa;
  *pa = *pb;
  *pb = t;
  return;
}

int main(void) {
  // because C is a call-by-value language, we need to use pointers in order to change
  // the value of a and b within the scope of main

  int a = 21;
  int b = 17;
  // when you call a function that accepts pointers in its args,
  // you need to use the unary ampersand & which is called a 'address-of' operator
  swap(&a, &b);
  printf("main: a = %d, b = %d\n", a, b);
  // this approach simulates "call-by-reference" behavior by generating object addresses,
  // passing those by value, and then de-referencing the copied addresses to access the
  // original objects
  return 0;
}