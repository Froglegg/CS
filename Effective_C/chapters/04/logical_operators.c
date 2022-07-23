#include <stdbool.h>
#include <stdio.h>
// && (AND) and || (OR) are used to test conditions
// test for "not equal to zero"
// these logical operators garuntee left-to-right evaluation, and can be used to
// short-circuit in cases where an evaluation an be deduced solely by the first operand
// this is a common technique for handling null pointers, e.g., this function can handle
// null pointers and will compile if passed a null pointer
bool pointer_value_is_number(int *ptr, int n) {
  return ptr && *ptr == n; // this doesn't dereference a null pointer
}
// using || can be useful when preventing unnecessary programming
// e.g., the expression `is_file_ready() || prepare_file()` will not run prepare_file()
// if is_file_ready() returns true

int main(void) {

  int *null_ptr = NULL;
  int value = 3;
  int *ptr = &value;
  // this should return 0 with no exceptions
  printf("%d\n", pointer_value_is_number(null_ptr, 3));
  // this should return 1
  printf("%d\n", pointer_value_is_number(ptr, value));

  return 0;
}