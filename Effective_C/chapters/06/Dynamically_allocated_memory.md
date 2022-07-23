# Storage Duration
Objects occupy storage, which might be RAM, ROM, or registers.
Storage of allocated duration has diff properties than storage of automatic
or static duration.

Automatic storage is declared within a block or as a function param.
The lifetime of these objects begin when the block in which they're
delcared begins execution, and ends when the block ends. If the block is
entered recursively, a new object is created each time, with it's own storage.

Objects with static storage are declared in file scope or using the `static` specifier. Their lifetime is entire execution of the program, and their value is initialized before program startup.

## Heap and Memory Managers
Dynamically allocated memory has **allocated storage duration**.
The lifetime of an allocated object extends from the allocation until the deallocation. Allocated memory comes from the **heap**, which is simply one or more large, subdividable blocks of memory that are manageed by the memory manager.

**Memory managers** are libraries that manage the heap for you by providing implementations of the standartd memeory mgmt functions described in the following sections. It runs as part of the client process. The manager will request one or more blocks of memory from the OS and then allocate this memory to the client process when it invokes a memory allocation function. Once memory has been allocated, the caller managers the memory until it is returned, and it is the caller's responsibility to dellocate the memory, although most implemetnations will reclaim memory when the program terminates.

Memory manager implementations typically implement a variant of a dynamic storage alogrithm described by Donald Knuth (1997) and uses boundary tags that allows the manager to coalesce two bordering unused blocks into a larger block to minimize **fragmentation**. Fragementation occurs when after allocating and de-allocating memory, many small blocks of memory are available but no big blocks are available, which leads to failures in large allocations.

## When to use dynamically allocated memory
Dynamically allocated memory is used when the exact storage requirements for a program are not known before runtime. It is less efficient than statically allocated memory, as the manager needs to find blocks of memory in the runtime heap, and then the caller must free those blocks, all of which requires additional processing. You should avoid using dynamically allocated memory if possible.

**Memory leaks** occur when dynamically allocated memory that's no longer needed isn't returned to the memory manager. If these memory leaks are severe, the manager will be unable to satisfy new requests for storage. Dynamically allocated memory also requires additional processes for housekeeping operations such as **defragmentation**, and uses extra storage for these control structures.

You would typically use dynamically allocated memory when the size of the storage is not known at compile tim ro the number of objects isn't known until runtime. E.g., to read a table from a file at runtime when you don't know the # of rows in the table, or to create linked lists, hash tables, binary trees, or other data structures for which the number of elements is unknown at compile time.

