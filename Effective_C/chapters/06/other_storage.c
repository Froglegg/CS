#include <ctype.h>
#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// alloca
// alloca function allows dynamic allocation during runtime from the stack instead of the
// heap. This memory is automatically released when the function that called alloca
// returns. It is an intrinsic (or built-in) function which means its implementation is
// handled by the compiler, which allows the compiler to subsitiute a sequence of
// auomtaically generated instructions for the original function call.

// Variable length arrays
// VLA's are arrays that you can specofy size at run time, must be declared at block
// scope or function call scope

// this array is allocated in the stack frame and freed when the current frame exits,
// simlar to the alloca function.

// you need to determine whether you have sufficient stack space in the worst case
// scenario before sing VLAs or alloca
void vla_test(size_t size) { int vla[size]; }

// you can use VLAs to generalize your functions, making them more useful. For exmaple,
// this matrix_sum function when passing a multidimensional array to a function, the size
// information is lost

int matrix_sum(size_t rows, size_t cols, int m[cols][rows]) {
  int total = 0;

  for (size_t r = 0; r < rows; r++) {
    for (size_t c = 0; c < cols; c++) {
      total += m[r][c];
    }
  }

  return total;
}

int main(void) {
  int m1[4][4];
  int m2[2][2];
  int sum = matrix_sum(4, 4, m1);
  printf("%d", sum);
  return EXIT_SUCCESS;
}