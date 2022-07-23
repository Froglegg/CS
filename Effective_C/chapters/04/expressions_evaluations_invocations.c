#include <stdio.h>
// simple assignment
// rvalue is converted to the type of the lvalue and then stored in the obkect designated
// by the lvalue lvalue can be thought of as the "left value", but should be thought of
// as the "locator value", because it must designate an object.
// an lvalue can also be an expression such as *(p+4), as long as it references an object
// in memory.
int i = 21;
// Evaluation means simplifying an expression down to a single value, and can involve
// value copmutations as well as the initiation of side effects.
// Side effects are changes to the state of the execution environment, and include
// writing to an object, accessing (r/w) a `volatile` qualified object, I/O, assignment,
// or calling a function that does any of these things.

// Functions are invocated by a "function designator", i.e., the function variables name
// In an expression, a function designator is converted to `pointer-to-function returning
// type` at compile time, and the value of each argument must align with the type of its
// parameters

// a "variadic" function can accept any number of arguments (printf is an example)

// We can pass one func to another:

int f(void) { return 0; }
// this code passes the address of a function designated by f to another function, g
// the function g accepts a function pointer to a function that accepts no args and
// returns int.
void g(int (*func)(void)) {
  if (func() != 0)
    printf("g failed\n");
  else
    printf("success!");
}
// A function passed as an argument is implicitly converted to a function pointer.
// the function of g makes this explicit, however you could also define this behavior
// implicitly:
void g_implicit(int func(void)) {
  if (func() != 0)
    printf("g failed\n");
  else
    printf("success!");
}

int main(void) {
  g(f);
  g_implicit(f);
}
