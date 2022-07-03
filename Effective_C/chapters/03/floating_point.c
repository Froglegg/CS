#include <limits.h>
#include <math.h>
#include <stdio.h>
// floating-point is the most common representation of real numbers in computers
// it is a technique that uses scientific notation to encode numbers with a base number
// and an exponent
// for example, 123.456 can be represented as 1.23456 * 10^2

// Annex F is the most common floating point format

// C has three fp types: float, double and long double
// float type uses single-precision; double uses more, long double even more
// double is most common and is the default choice

// Floating point types can also represent values that are not fp numbers, such as +/-
// Infinity and NaN values, and NaN can be silent or signaling
// subnormal floats are the domain of numbers (-FLT_MIN, 0) U (0, FLT_MIN)

// one way to classify the fp value you're dealing with is to use the `fpclassify` macro
const char *show_classification(double x) {
  switch (fpclassify(x)) {
  case FP_INFINITE:
    return "Inf";
  case FP_NAN:
    return "NaN";
  case FP_NORMAL:
    return "normal";
  case FP_SUBNORMAL:
    return "subnormal";
  case FP_ZERO:
    return "zero";
  default:
    return "unknown";
  }
}

// floating point constants
float f1 = 15.75;
float f2 = 1.575E1;
float f3 = 1675e-2;
float f4 = -2.5e-3;
float f5 = 25E-4;
int main(void) {
  double x = __FLT_MIN__ + 1;
  printf("%s\n", show_classification(x));

  printf("%f\n", f1);
  printf("%f\n", f2);
  printf("%f\n", f3);
  printf("%f\n", f4);
  printf("%f\n", f5);

  return 0;
}