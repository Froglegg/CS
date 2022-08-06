// system headers already have header guards so don't worry about them
#include <stdio.h>
// use header guards
#ifndef BAR_H
#define BAR_H
int print_bar(void) {
  puts("bar!");
  return 0;
}

#endif