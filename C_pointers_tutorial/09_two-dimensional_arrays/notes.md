# Pointers and two-dimensional arrays
One dimensional arrays in memory are allocated as contigous blocks of memory in which each block is sizeof(array type)

A pointer to an array points to the address of the base element in an array, and can be used to access elements via dereferencing and step through an array

Two dimensional arrays, e.g. an array of arrays, `int B[2][3]` (two 1-D arrays of three integers each), are allocated contiguously as well, with one block for each 1st dimensional array, and blocks for each item within each 2nd dimensional array.

For example, in `int B[2][3]`, two blocks of 12 bytes (sizeof(int) * 3) for both arrays would be allocated, allocating in total a contiguous block of 24 bytes for the 2D array.

To declare a pointer to the base element in the 2D array `int B[2][3]`, you would need to typecast it as a pointer to an array of 3 characters, such as: `int (*p)[3] = B`.

When conducting pointer arithmetic on 2D arrays, the operand is coerced into the size of the 1D array (in our example, int[3]).
Incrementing the 2D array B with `B+1` would yield a pointer to the next element in the second dimension, i.e., `B+1 = &B[0] + sizeof(int[3]) = &B[1][0] || &B[1]`. Printing `*(B-1)` prints the address of `B[1]`.



