#include <stdio.h>
// type casts
// to perform a type cast, we precede an expresssion by a parenthesized type name

void cast_example(void) {
  double x = 1.2;
  int sum = (int)x + 1; // explicit conversion
  printf("%d", sum);
}

// conditional operator (?:) or ternary (takes three operands) returns a result based on
// a condition
// e.g., `result = condition ? valueReturnedIfTrue : valueReturnedIfFalse;`

// relational operators
// these are: ==, !-, <, >, <=, and >=
// compouned assignment
// +=, -=. *=, /=, %=

// Comma operator
// commas are used as opartors and as a way to separate items in a list
// e.g., f(a, (b, c), d) or [1,2,3]
