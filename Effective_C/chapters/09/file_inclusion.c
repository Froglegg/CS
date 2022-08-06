#include "foo_bar.h"
// use .h header file extension for header files to be included by the preprocesser in
// the source file. This is the most common way to share external declarations of
// functions and objects with other parts of the program.
int main(void) {
  print_foo();
  print_bar();

  return 0;
}