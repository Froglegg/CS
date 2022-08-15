# Using pointers as function arguments (call by reference)
This is a use case scenario for pointers using them as function arguments (calling by reference)

Memory is divided into four parts
1. Heap
2. Stack
3. Static/Global
4. Code (text)

If we do not declare a variable inside a function, it is a global variable

Stack is where all the local variables go (static)

During runtime, application can use Heap to allocate memory

During compile time, the stack is used for allocation/deallocation

Each function has a stack frame (a block within the stack for allocation).

You cannot access a variable outside its stack frame. After a function returns, it eliminates its stack frame.

When we call a function, the calling function argument is mapped to the formal argument in the callee, i.e., the value of the arg is mapped to the callee arg, i.e., the function is called by value.

We need to pass addresses of variables we want to mutate in called functions in order to mutate their values. This is "call by reference".