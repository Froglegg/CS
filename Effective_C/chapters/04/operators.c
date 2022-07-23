#include <math.h>
#include <stddef.h>
#include <stdio.h>
// increment and decrement operators can have postfix or prefix operators
// a prefix performs the operation before returning the value, while a postfix returns
// the value and then performs the increment
void increment_decrement(void) {
  int i = 5;
  int e;
  e = i++; // i has value 6, e has value 5
  printf("e: %d, i: %d\n", e, i);
  e = i--; // i has value 5, e has value 6
  printf("e: %d, i: %d\n", e, i);
  e = ++i; // prefix, i has value 6, e has value 6
  printf("e: %d, i: %d\n", e, i);
  e = --i; // prefix, i has value 5, e has value 5
  printf("e: %d, i: %d\n", e, i);
}
// precendence and associativity
// think pemdas, but also with various programmatic operations
// things get weird with postfix and prefix increment / decrement operators.
// observe what happens when using a postfix vs prefix operation on a pointer variable

void precedence_example(void) {
  char abc[] = "abc";
  char xyz[] = "xyz";

  char *p = abc;
  // the pointer is dereferenced, producng 'a'
  // it is then incremented with a prefix expression, increments and then returns,
  // producing the value 'b'
  printf("%c", ++*p);
  // returns 'b'

  // here, we use a postfix, so the value is returned first before being incremented
  p = xyz;
  printf("%c", *p++);
  // returns 'x'
}

// order of evaluation of the operands of any C operator or subexpressions is
// unspecified, which allows the compiler to pick and choose them in any order that is
// fastest. The oreder of evaluation is contasined by operator precedence and
// associativity, which is controlled by us the programmers.
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
// the global variable glob is accessed by both f and g, which means they share state
// values may differ between compilations, and may be 42 or 52
int glob;
int f(void) { return glob + 10; }
int g(void) {
  glob = 42;
  return glob;
}
void eval_order_bad_example(void) {
  int max_value = MAX(f(), g());
  printf("%d", max_value);
}
// to garuntee predictable, portable behavior, wrie it in this way
// in this revised program, the f call is garunteed to be sequenced before the g call,
// and the f call must compelete before the g call is made.
// this will always return 42
void eval_order_good_example(void) {
  int f_val = f();
  int g_val = g();
  int max_value = MAX(f_val, g_val);
  printf("%d", max_value);
}

// use sizeof to get the size of a type
// use size_t type from <stddef.h> for declaring sizeof objects
size_t get_size_of(x) { return sizeof(x); }
int main(void) {
  //   increment_decrement();
  //   precedence_example();
  //   eval_order_bad_example();
  // eval_order_good_example();
  int i = 6;
  // int type should return 4 bytes
  size_t test = get_size_of(i);
  printf("%lu\n", test);
  // this will return bits, int type should have 32 bits
  long unsigned int test2 = __CHAR_BIT__ * test;
  printf("%lu\n", test2);
  return 0;
}
