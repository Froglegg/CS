# Pointers and Dynamic Memory
The memory that is assigned to a program can be divided into four segments.

1. Code(text) instructions
2. Static / Global
3. Stack (function calls, stack frames, local variables)
4. Heap (free store / dynamic memory, this can be allocated during runtime with malloc)

Stack overflow can occur during infinite recursion (call stack exceeds allocated memory for stack, segmentation fault and crash)

(The term "heap" has nothing to do with the "heap" data structure, however, "stack" is an implementation of a stack data structure)

To use dynamic memory in C, we must know four functions:
- malloc
- calloc
- realloc
- free
In C++, you only need:
- new
- delete





