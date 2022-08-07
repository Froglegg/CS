#include "isprime.h"
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

static void print_help(void) {
  printf("%s", "primetest num1 [num2 num3 ... numN]\n\n");
  printf("%s", "Tests positive integers for primality. Supports testing ");
  printf("%s [2-%llu].\n", "numbers in the range", ULLONG_MAX);
}
// Converts a string argument arg to an unsigned long long value referenced by val.
// Returns True if the argument conversion succeeds, else false if it fails
static bool convert_arg(const char *arg, unsigned long long *val) {
  char *endptr;
  // strtoull (string to unsigned long long) sets end_ptr to null and returns 0 for
  // failed conversions
  *val = strtoull(arg, &endptr, 10);
  // val should not be less than or equal to 1 if we are testing for primes
  if (endptr == NULL || *val <= 1)
    return false;
  // succesful conversion
  return true;
}

// this function is repsonsbile for allocating a sufficiently large buffer to hold the
// array of integers. It also handles all error conditions, such as running out of memory
// or failing to voenrt an argument. If the function suceeds, it returns an array of
// integers to the caller and writes the converted number of args into the num_args
// parameter. The returned array is allocated storage and must be deallocated when no
// longer needed.
static unsigned long long *convert_command_line_args(int argc, const char *argv[],
                                                     size_t *num_args) {
  *num_args = 0;
  if (argc <= 1) {
    // no command line args given (first arg is name of prgoram being executed)
    print_help();
    return NULL;
  }
  // we know that the max number of args th user could have passed, so allocate an array
  // large enough to hold all of the elements. Subtract one for the program name itself.
  // If the allocation fails, treat it as a failed converstoin (it is okay to call
  // free(NULL))
  unsigned long long *args =
      (unsigned long long *)malloc(sizeof(unsigned long long) * (argc - 1));
  bool failed_conversion = (args == NULL);
  for (int i = 1; i < argc && !failed_conversion; ++i) {
    // attempt to convert arg to integer. If we couldn't set failed_conversion to true
    unsigned long long one_arg;
    // unary pipe | is the bitwise OR operator
    failed_conversion |= !convert_arg(argv[i], &one_arg);
    args[i - 1] = one_arg;
  }
  if (failed_conversion) {
    // free the array, print the help, and bail out
    free(args);
    print_help();
    return NULL;
  }

  *num_args = argc - 1;
  return args;
}

// program implementation
int main(int argc, const char *argv[]) {
  size_t num_args;
  unsigned long long *vals = convert_command_line_args(argc, argv, &num_args);

  if (!vals)
    return EXIT_FAILURE;

  for (size_t i = 0; i < num_args; ++i) {
    printf("%llu is %s.\n", vals[i],
           is_prime(vals[i], 100) ? "probably prime" : "not prime");
  }
  // deallocate memory allocated by convert_command_line_args
  free(vals);
  return EXIT_SUCCESS;
}
