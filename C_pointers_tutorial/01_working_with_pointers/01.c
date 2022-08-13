#include <stdio.h>

int main(void) {

  //   int a;
  //   int *p;
  //   p = &a;
  //   a = 10;
  //   printf("%d\n", *p);
  //   printf("%d\n", &a);

  //   // you can use dereferencing to set a value as well
  //   *p = 12;
  //   // we have modified a value using a pointer
  //   printf("%d\n", a);

  //   int b = 20;
  //   *p = b;
  //   // you can use another variable to modify a value with a pointer
  //   printf("value of a is %d", a);

  // increment and decrement a pointer variable
  int a = 10;
  int *p = &a;

  p = &a;
  // e.g., 2002
  printf("address p is %d\n", p);
  printf("size of integer is %d\n", sizeof(int));
  printf("value at address p is %d\n", *p);
  // this will incremeent address by 4 bytes, e.g., 2006
  printf("address p+1 is %d\n", p + 1);
  // this will access a gargbage value
  printf("value at address p + 2 is garbage: %d\n", *(p + 2));

  return 0;
}