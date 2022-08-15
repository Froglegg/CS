#include <stdio.h>

void A(void) { printf("Hello"); }
// function pointer as argument
void B(void (*ptr)()) {
  // call-back function that ptr points to
  ptr();
}

int main(void) {
  B(A); // A is callback function
  return 0;
}