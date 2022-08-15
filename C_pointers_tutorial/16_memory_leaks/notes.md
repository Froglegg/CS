# Memory leaks
A memory leak is a situation in which we get some memory on the heap (malloc), but do not free it when we are done using it (free).

During program execution, if memory is allocated within a loop and is not freed afterwards, the program will allocate blocks of memory on the heap over and over again, taking up memory unnecessarily (memory leak)