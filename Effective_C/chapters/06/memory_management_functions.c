#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
  char c[10];
  int i;
  double d;

} widget;
// malloc function allocates space for an object of a specified size whose initial value
// is indeterminate
int malloc_test(void) {
  // all memory allocation functions accept an arg of type size_t that specifies the
  // number of bytes of memory to be allocated. For portability, we use the sizeof
  // operator, as type sizes may differ across implementations
  widget *p = malloc(sizeof(widget));
  // the malloc function either returns a NULL ptr to indicate an error or a pointer to
  // the allocated space
  if (p == NULL) {
    // handle allocation error
    puts("NULL POINTER! MALLOC ERROR!");
    return EXIT_FAILURE;

  } else {
    // after succesful allocation, we can store widgets to the address space.
    // for example, p->i would access the int member of widget, while p->d would access
    // the double member.
    p->i = 11;
    p->d = 420.69;
    int i_val = p->i;
    double d_val = p->d;
    printf("\nint value: %d, double value: %f", i_val, d_val);
    // we can also assign values to the struct array using a similar syntax
    for (int i = 0; i < sizeof(p->c); i++) {
      p->c[i] = i;
      printf("\n%d", p->c[i]);
    }
  }
  // you can store the return value from malloc as a void pointer to avoid explicitly
  // declaring a type for the referenced object
  // sizeof(void) is 1 byte in the Gnu Compiler Collection (GCC) and compilers designed
  // to be compatabile with it (e.g., clang, etc.),
  void *vp = malloc(sizeof(void));
  if (vp == NULL) {
    // handle allocation error
    puts("NULL POINTER! MALLOC ERROR!");
    return EXIT_FAILURE;
  }
  // once we copy an object into our void pointer, it'll have the effective type of said
  // object.
  widget w = {"abc", 9, 3.2};
  // memcpr copies n characters from memory area src to memory area dest.
  memcpy(vp, &w, sizeof(widget));
  // we'll need to explicitly coerce the type of vp from void * to widget *
  printf("vp.i = %d\n", ((widget *)vp)->i);

  // deallocate memory from the free store (heap)
  // ALWAYS DO THIS!!!
  free(p);
  free(vp);
  // set to NULL to avoid danglers
  p = NULL;
  vp = NULL;
  return EXIT_SUCCESS;
}

int str_copy_test(void) {
  // reading unitialized memory
  char *str = (char *)malloc(16);
  if (str) {
    // don't assume malloc returns 0's
    strncpy(str, "123456789abcdef", 15);
    // set null terminating char \0
    str[15] = '\0';
    printf("\nstr = %s\n", str);
    free(str);
    // set to null to avoid dangling pointers
    str = NULL;
    return EXIT_SUCCESS;
  }
  return EXIT_FAILURE;
}

// alligned_alloc
// some hardware has stricter than normal memory alignment requirements.
// alligned_alloc is similar to malloc but has a parameter for alignement to override
// the deafult alignments for standard type
// we won't demo it here

// calloc
// allocates storage for an array of nmemb (number elements) objects, each of whose size
// is size bytes void *calloc(size_t nmemb, size_t size)
// The calloc() function in C is used to allocate a specified amount of memory and then
// initialize it to zero. The function returns a void pointer to this memory location,
// which can then be cast to the desired type.

// realloc
// this function increases or decreases the size of previously allocated storage. It
// tkaes a pointer to some memory allocated by an earlier call and a size. You can use
// this function to grow or shrink the size of an array.
// realloc return a NULL pointer if the pointer is succesfully
int realloc_test(void) {
  void *p2;
  void *p = malloc(100);
  // resize memory to new_size
  size_t new_size = 1000;
  p2 = realloc(p, new_size);
  // if realloc returns a NULL pointer, that means allocation failure and we need to free
  // p
  if ((new_size == 0) || p2 == NULL) {
    free(p);
    return NULL;
  }
  // else, reallocation was succesfl and we can reassign p to the newly reallocated
  // storage and continue program execution
  p = p2;
  // always free your allocation before exiting!!
  free(p);
  // set to null to avoid dangling
  p = NULL;
  return EXIT_SUCCESS;
}

// reallocarray
//  reallocate memory for array function also provides overflow checking

// free
// the free function deallocates memory. It's important because it allows memory to be
// reused, reducing the chance you'll exhaust available memory and makes for more
// efficient use of the heap. Don't call free() on the same pointer more than once,
// leading to a double-free vulnerability pointers that are already freed are called
// "dangling pointers" to limit dangling pointers, set the poitner to NULL after
// completing a call to free

int main(void) {
  malloc_test();
  str_copy_test();
  realloc_test();
  return EXIT_SUCCESS;
}