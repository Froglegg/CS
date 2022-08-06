#include <math.h>
#include <stdio.h>
// the #define directive defines a macro
// Macros can be used to define constant values or function-like constructs with generic
// params. The macro definition contains a (possibly empty) replacement list, a code
// pattern that's injected into the translation unit when the preprocessor expands the
// macro: #define identifier replacement-list
// e.g.,
#define ARRAY_SIZE 100
void array_macro_test(void) { int array[ARRAY_SIZE]; }

// you can specify macros in clang command line like so: `-DARRAY_SIZE=100`
// the scope of a macro lasts until #undef directive or end of the translation unit

// a function-like macro is parameterized and requires passing a possibly empty set of
// arguments when you invoke it.
// e.g.,
#define FOO (1 + 1)
#define BAR(x) (1 + (x))
void foo_bar_macro_test(void) {
  int i = FOO;
  int j = BAR(10);
  int k = BAR(2 + 2);
  printf("i:%d\n j:%d\n k:%d\n", i, j, k);
}

// you can join multiple source lines by using backslash character, e.g.,
#define cbrt(x)                                                                         \
  _Generic((x), long double : cbrtl(x), default : cbrt(x), float : cbrtf(x))
// undefine macro
#undef cbrt

// Macro replacement
// Macros let you perform operations using the symbols in the source file
// you can create new variable names or reference the source file and line number of the
// macro. When a preprocessor encounters a macro identifier, it will invoke and then
// expand the identifier to replace it with the tokens from the replacement list, if any

// for function like macros any parameter in the replacement list preceded by a # is
// replaced with a string literal preprocessing token that contains the text of the
// argument preprocessing tokens (a process sometimes called stringizing)
#define STRINGIZE(x) #x
void test_stringize(void) {
  const char *str = STRINGIZE(12);
  // reeulsts in "12"
  printf("\n%s", str);
}
// it also deletes all instances of the ## preprocessing token in the replacement list,
// concatenating the preceding tokens with the following token, which is called token
// pasting
#define PASTE(x, y) x##_##y
void test_paste(void) {
  // token pasting,
  int PASTE(foo, bar) = 69;
  // reeulsts in 69
  printf("\n%d", foo_bar);
}

// Type generic macros
// you might sometimes need to alter the behavior of an algorithm based on the types of
// the arguments involved. For example, <math.h> has three sin functions (sin, sinf,
// sinl) because each of the three floating point types have a different precision.

// By using generic selection expressions, you can define a single function-like
// identifier that delegates to the correct underlying implementation based on the
// argument type called.

// e.g., define sin as a macro function accepting _Generic type with three different
// type-based implementations of sin from math.h
#define sin(x) _Generic((x), float : sinf, double : sin, long double : sinl)(x)
void test_generic_macro(void) {
  float f = sin(1.5708f);
  double d = sin(3.14159);
  printf("\n%f", f);
  printf("\n%f", d);
}

int main(void) {

  foo_bar_macro_test();
  test_stringize();
  test_paste();
  test_generic_macro();
  return 0;
}
