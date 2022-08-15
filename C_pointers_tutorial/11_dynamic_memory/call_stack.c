#include <stdio.h>
// global total
int total;
int square(int x) { return x * x; }
int squareOfSum(int x, int y) {
  // stack frame z
  int z = square(x + y);
  return z;
}
int main(void) {
  // call main, then squareOfSum, etc
  int a = 4, b = 8;
  total = squareOfSum(a, b);
  printf("Total: %d\n", total);
  return 0;
}