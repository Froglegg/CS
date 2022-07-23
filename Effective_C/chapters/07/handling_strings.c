#include <stdio.h>
#include <stdlib.h>
// string.h for narrow string handling funcs
#include <string.h>
// wide char header file for wide string handling funcs
#include <ctype.h>
#include <wchar.h>

// legacy string.h and wchar.h functions lacked size-checking and can lead to misuse /
// buffer overflows
// C11 introduced Annex K bounds checking interfaces, which provides alternative library
// functions intended to pormote safer, more secure programming by requiring you to
// rpovide the length of output buffers, and validating that these buffers are
// adequeatley sized to contain the output form these funcs. for example, Annex K defines
// strcpy_s, strcat_s, strncpy_s, and strncat_s whereein _s means "safe"

// POSIX also defines several stirng-handling funcs, such as strdup and strndup that can
// be used on linux / unix and other POSIX compliant platforms

void size_and_length_funcs(void) {
  // strings have both a size (number of bytes allocated to backing storage array) and a
  // length (number of characters in a string)
  char str[100] = "Here comes the sun";
  size_t str_size = sizeof(str); // str_size is 100
  size_t str_len = strlen(str);  // str_len is 18

  // dynamically allocating storage for narrow strings
  char dynamic_string[] = "Here comes the sun";
  //   add 1 for terminating null character
  char *string = malloc(strlen(dynamic_string) + 1);
  free(string);
  string = NULL;

  // calculating size of dynamically allocated memory
  // one way is to store size when allocating and reuse this value later
  // lets use the size of a string to copy to another destination
  char str_2[100] = "Here comes the sun";
  //   add 1 for terminating null character
  size_t str_2_size = strlen(str_2) + 1;
  char *dest = (char *)malloc(str_2_size);
  if (dest) {
    strcpy(dest, str_2);
    printf("%s", dest);
  }
  free(dest);
  dest = NULL;
}

// gets function is bad because it has no way of knowing how large a destination array
// is when getting user input, it will just aaccept and write beyond the end of an
// array object. the get_s function is safer (Annex K bounds checking interface),
// checks the array bounds for input, see example
void gets_test(void) {

  char response[8];
  size_t len = sizeof(response);
  puts("WRITE SOMETHING!!: ");
  // gets would overwrite array, use fgets
  fgets(response, len, stdin);
  printf("\nYOUR RESPONSE: %s", response);
  if (response[0] == 'n')
    exit(0);
}

void POSIX_funcs(void) {
  // strdup duplicates a string, returns a pointer to a string that contains a duplicate
  // of the argument
  const char *temp = getenv("USER");
  if (temp != NULL) {
    char *tmpvar = strdup(temp);
    if (tmpvar != NULL) {
      printf("TMP = %s.\n", tmpvar);
      free(tmpvar);
    }
  }
  // could also just
  char *whatever = strdup("HEY");
  printf("%s", whatever);
  free(whatever);
}

int main(void) {
  //   size_and_length_funcs();
  //   gets_test();
  POSIX_funcs();
  return 0;
}