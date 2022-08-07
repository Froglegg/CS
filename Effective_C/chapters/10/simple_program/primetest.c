/*

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

static unsigned long long power(unsigned long long x, unsigned long long y,
                                unsigned long long p) {
  unsigned long long result = 1;
  x %= p;

  while (y) {
    if (y & 1)
      result = (result * x) % p;
    y >>= 1;
    x = (x * x) % p;
  }
  return result;
}

static bool miller_rabin_test(unsigned long long d, unsigned long long n) {
  unsigned long long a = 2 + arc4random() % (n - 4);
  unsigned long long x = power(a, d, n);

  if (x == 1 || x == n - 1)
    return true;
  while (d != n - 1) {
    x = (x * x) % n;
    d *= 2;

    if (x == 1)
      return false;
    if (x == n - 1)
      return true;
  }
  return false;
}

// public interface function is_prime
// n is the number to test, k is number of times to test
bool is_prime(unsigned long long n, unsigned int k) {
  if (n <= 1 || n == 4)
    return false;
  if (n <= 3)
    return true;

  unsigned long long d = n - 1;
  while (d % 2 == 0)
    d /= 2;

  for (; k != 0; --k) {
    if (!miller_rabin_test(d, n))
      return false;
  }
  return true;
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

*/
