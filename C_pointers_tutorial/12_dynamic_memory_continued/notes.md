# malloc, calloc, realloc, free
To use dynamic memory in C, we must know four functions:
- malloc(size_t size) -> void * // returns void pointer to the address of first byte in allocated memory block of size_t size
- calloc(size_t nmemb, size_t size) -> void * // same as malloc but also includes number of elements (nmemb), and initializes all elements with 0
- realloc(void *ptr, size_t size) -> void * // change size of block of memory already allcoated, pass in pointer to original memory address and then new size
- free(void *ptr)