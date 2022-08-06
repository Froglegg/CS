// one problem you will face when writing header files is prventing programmers form
// including the same file twice or multiple times in a translation unit
// Header guards ensure that a file is included only once per translation unit, based on
// whether a header-specific macro is defined. If the macro is not already defined, you
// define it so that a subsequent test of the header guard will not include the code.

// e.g., in bar.h, I've defined the macro BAR_H
#include "bar.h"
// in foo.h, I've defined FOO_H
#include "foo.h"
// in foo_bar.h, I've included "bar.h" and "foo.h"
#include "foo_bar.h"
// the resulting translation unit will only have the one function from bar.h and the one
// function from foo.h
int main(void) {
  print_foo();
  print_bar();
  return 0;
}

// system headers, e.g., #include <stdio.h>, already have header guards so don't worry
// about them
