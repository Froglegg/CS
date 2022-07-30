#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

// fscanf is the corresponding input version of the fprintf function and is used to read
// formatted input from a stream and uses a format string that tells the function how
// many args to expect and their type, and how to convert them for assignment
int fscanf_test(void) {
  FILE *ptr = fopen("abc.txt", "r");
  if (ptr == NULL) {
    printf("no such file.");
    return 0;
  }

  /* Assuming that abc.txt has content in below
     format
     NAME    AGE   CITY
     abc     12    hyderabad
     bef     25    delhi
     cce     65    bangalore */
  char buf[100];
  while (scanf(ptr, "%*s %*s %s ", buf) == 1)
    printf("%s\n", buf);

  return 0;
}

int main(void) {
  fscanf_test();
  return 0;
}