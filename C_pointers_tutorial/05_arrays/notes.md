# Pointers and Arrays
Arrays are stored as contiguous blocks of memory

When we declare an array, e.g., `int A[n]`, we allocate `n` blocks of memory, where address space for each block is determined by the type (e.g., `int` would have a block size of 4 bytes, so an integer array of size `5` would occupy 20 bytes)

We can use pointer arithmetic to access elements within and step through an array if we know the length of the array and the size of the element type