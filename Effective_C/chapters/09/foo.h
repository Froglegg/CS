// system headers already have header guards so don't worry about them
#include <stdio.h>
// use header guards
#ifndef FOO_H
#define FOO_H

int print_foo(void) {
  puts("foo!");
  return 0;
}

#endif