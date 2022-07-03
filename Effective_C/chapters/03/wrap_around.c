// limits.h has the min and max values for all integer types
// a representable value is one htat van be represented int he number of bits available
// to an object of a particular type
// to write portable code, use the limits.h constants
#include <limits.h>
#include <stdio.h>
//
int main(void) {
  // wraparound occurs when you go beyond or below the max or min values of an integer
  // type
  unsigned int ui = UINT_MAX; // 4.294 billion on x86
  ui++;
  printf("ui = %u\n", ui); // wraps around to zero
  ui--;
  printf("ui = %u\n", ui); // wraps back around to 4.294 billion

  // signed ints can be called with just "int"
  int i = INT_MAX;
  i++;
  printf("%d", i); // wraps around to -2.147 bil
  // use short or long types to save storage and increase performance
  signed char sc = SCHAR_MAX;    // 128
  short int si = SHRT_MAX;       // 32768
  long int li = LONG_MAX;        // same as int, 2.147 billion
  long long int lli = LLONG_MAX; // 2^63, pretty big probably would never use this

  return 0;
}
