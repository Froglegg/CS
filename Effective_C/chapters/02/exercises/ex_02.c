#include <stdio.h>

int func_1(void) { return 1; };
int func_2(void) { return 2; };
int func_3(void) { return 3; };
// declare an array of 3 pointers to int(void) functions
// pointers hold the address of other variables, rather than variable values
int (*pointer_func_array[3])(void);
// the * operator is known as the "indirection operator", the "dereference operator", or
// the "value at address" operator
// it is used for obtaining the value of a variable at the address to which the pointer
// points

int main(void) {

  int result;

  // set the address of (&) our functions to the three allocated spaces in our pointer
  // array
  pointer_func_array[0] = &func_1;
  pointer_func_array[1] = &func_2;
  pointer_func_array[2] = &func_3;

  for (int i = 0; i < 3; i++) {
    // to call our functions in our array of pointers, we need to dereference them using
    // the indirection (value at address) operator
    result = (*pointer_func_array[i])();
    // this returns the functions themselves, which we can then execute()
    printf("%d", result);
  }
}
