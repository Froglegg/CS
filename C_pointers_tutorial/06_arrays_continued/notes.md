# Arrays as function arguments
When the compiler sees an array as function argument, it just creates a pointer to the data type of the array, and the compiler just copies the address of the first element of the array in the calling function.

The compiler implicitly converts the array argument into a pointer to the type of the array. Arrays are *always* passed as reference parameters (are passed by reference).

This makes sense, because arrays can be large parameters, and so copying the entire value into a callee stack frame could be expensive. So they just copy the reference to the base element of the array.