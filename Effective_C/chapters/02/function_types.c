// function types are derived types, in this case, the type is derived from the return
// type and the number / types of its parameters
// use function declarator to declare name of function and return type, e.g.,
int some_func(void); // returns a n int, takes no arguments
// this returns a pointer to an int, NOTE do not declare a func with empty params! USE
// VOID
int *func_int_pointer();
// these dont return anything at all
void g(int i, int j);
void h(int, int);