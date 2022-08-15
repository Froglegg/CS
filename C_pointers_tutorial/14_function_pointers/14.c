#include <stdio.h>

int Add(int a, int b) { return a + b; }
void Hello() { printf("Hello"); }

int main(void) {
  // pointer to function that should take (int, int) as an argument and return int
  int (*p)(int, int);
  // initialize function pointer
  //   p = &Add;
  // we could, but we don't need to use & operator, as the function name without parens
  // returns an address
  p = Add;

  // we can use p to execute function Add by dereferncing the function pointer and
  // passing arguments
  // we could, but we don't need to dereference the pointer, as calling and passing args
  // to the address at p will execute the function
  //   int c = (*p)(2, 3);
  int c = p(2, 3);
  // this should return 5
  printf("%d\n", c);
  // using with a void function
  void (*ptr)() = Hello;
  ptr();

  return 0;
}