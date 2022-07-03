#include <limits.h>
#include <stdio.h>
// overflow occurs when a signed integer operation results in a value that cannot be
// represented in the resulting type
// e.g., this function-like macro can overflow when used with
// negative values
#define Abs(i) ((i) < 0 ? -(i) : (i))
// this implementation takes a type dependent flag argument, which matches the *_MIN
// macro, which matches the type of the first argument. By including a type-specific
// limit to our function, we can avoid overflow
#define AbsM(i, flag) ((i) >= 0 ? (i) : ((i) == (flag) ? (flag) : -(i)))

void recover(void) { printf("HEY there"); }
int main(void) {
  // this operation is OK
  signed int si = -25;
  signed int abs_si = Abs(si);
  printf("%d\n", abs_si);
  // this operation results in signed integer overflow, which is undefined behavior in C
  // this will result in a "silent wrapping" of min_int, or trap, or both
  // a trap is an interruption of the program.
  signed int min_int = INT_MIN;
  signed int abs_min_int = Abs(min_int);
  printf("%d\n", abs_min_int); // returns -2147483648, not an absolute value...

  // use the special AbsM function to handle overflows
  signed int test_si = INT_MIN; // try INT_MIN to trigger the problem case
  signed int abs_si_test = AbsM(test_si, INT_MIN);
  if (abs_si_test == INT_MIN)
    printf("SPECIAL CASE"); // special case, here we may need to do some special stuff
  printf("%d\n", abs_si_test);

  return 0;
}
