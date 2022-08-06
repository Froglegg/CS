// frequently, you'll need to write code to support different implementations, e.g., for
// different target architectures. You can conditionally include source code by including
// a predicate condition using #if #elif and #else. These are typically used alongside a
// #defined directive that is used to dtermine whether a iven identifier is the name of a
// defined macro.
// e.g.
#if defined(_WIN32)
#include <Windows.h>
#elif defined(__ANDROID__)
#include <android/log.h>
#endif
// if neither of these are defined, the output is empty

// you can write #ifdef() or #ifndef() as shorthand for #if defined() and #if !defined()
// respectively

// We may need to generate an error if the preprocessor can't take any of the conditional
// branches and/or no reasonable fallback behvaior exists

// e.g., select betweeen including C standard library header <threads.h> or the POSIX
// threading library <pthread.h>
// if neither option is availabl,e you shuold alert the programmer porting the system
// that the code must be repaired
#if __STDC__ && __STDC_NO_THREADS__ != 1
#include <threads.h>
#elif POSIX_THREADS == 200809L
#include <pthread.h>
#else
// this will show red squiggles
#error "Neither <threads.h> nor <pthread.h> is available"
#endif
