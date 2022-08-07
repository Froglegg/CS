
// static and runtime assertions
// static assertions are checked at compile time, runtime assertions at runtime
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <string.h>

// if static assertion is equal to 0 (false), then it will produce the message
void staticAssertionTest(void) {
  struct packed {
    unsigned int i;
    char *p;
  };
  // you can use static assertions to validate assumptions at compile time
  // VSCode will throw red squiggles here
  //   static_assert(sizeof(struct packed) == sizeof(unsigned int) + sizeof(char *),
  //                 "struct packed must not have any padding");
}

void clear_stdin(void) {
  // when getting stdin input, we use getchar until we encounter EOF
  // however, on some implementations, we could get false positives, as the C standard
  // allows for unsigned char and int to have the same range
  // use static assert to test for this unusual condition within the do while loop
  int c;

  do {
    c = getchar();
    // placing static assertions have no effect on runtime efficiency because the
    // assertion takes place at compile time
    static_assert(UCHAR_MAX < UINT_MAX, "FIO34-C Violation");
  } while (c != EOF);
}

void bounds_checking(void) {
  static const char prefix[] = "Error No: ";
#define ARRAYSIZE 14
  char str[ARRAYSIZE];

  // ensure that str has sufficient space to store at least one additional character for
  // an error code
  static_assert(sizeof(str) > sizeof(prefix), "str must be larger than prefix");
  strcpy(str, prefix);
}

// using runtime assertions to verify program conditions
void *dup_string(size_t size, char *str) {
#define LIMIT 50
  assert(size <= LIMIT && "size is larger than the expected limit.");
  assert(str != NULL && "the caller must ensure str is not NULL.");
}

// you should disable assertions before code is deployed by defining the NDEBUG macro
// (typically as a flag passed to the compiler).

int main(void) {

  //   clear_stdin();
  bounds_checking();

  return 0;
}