#include <stdio.h>

int main(void) {
  int x = 5;
  int *p;
  p = &x;
  // set x to 6
  *p = 6;
  // declare a pointer to a pointer using double asterisks **
  int **q;
  q = &p;
  // declare a pointer to a pointer to a pointer with triple asterisks... we can go on
  // like this
  int ***r;
  r = &q; // q is int** type;

  // dereferencing pointer to int p will return the value at &x, which is 6
  printf("%d\n", *p);
  //   dereferencing pointer to pointer q will return &x, which is the value of pointer p
  printf("%p\n", *q);
  // dereferencing pointer to pointer q twice will return the value at &x, which is 6
  printf("%d\n", *(*q));
  // dereferencing pointer to pointer to pointer r twice will return &x, whic is the
  // value of pointer p
  printf("%p\n", *(*r));
  // derefrencing pointer to pointer to pointer r three times will return the value at
  // &x, which is 6
  printf("%d\n", *(*(*r)));

  // you can modify original value by dereferncing nested pointers
  ***r = 10;
  printf("X is now equal to: %d\n", x);

  return 0;
}