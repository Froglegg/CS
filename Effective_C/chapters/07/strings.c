#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// C has no primitive string type and probably never will. Instead, it implements strings
// as arrays of characters.

// C has two types of strings: narrow and wide

// a narrow str has the type array of char (char[]) and consists of a contiguous sequence
// of characters that include a terminateing null cahracter
// a pointer to a string points to its initial character
// the size of a streing is the number of bytes allocated tot he backing arrays torage
// the length of a string is the nuymber of code units (bytes) preceding the first null
// character.

// a wide str has the type array of wchar_t, and is the same as a narrow string except
// uses UTF-16 wchar_t

// a string literal is a string constant represented by a sequcen of multibyte chracters
// enclosed in double quotes, for exmaple, "ABC". Do not attempt to modify string
// literals, undefined behavior.

void stringliteral(void) {
// string literals often initialize array variables
#define STRING_INIT "abc"
#define CHAR_ARRAY_INIT "abcd"
  // this declaration has the exact size necessary to initialize the array to the stirng
  // variable, including the space for the trailing null byte
  const char string[4] = STRING_INIT;
  // this will print abc
  //   printf("\n%s", string);

  //   if you add another character to the string literal used to initialize the array,
  //   it displaces the trailing null byte and you no longer have a string, you have a
  //   character array
  const char character_array[4] = CHAR_ARRAY_INIT;
  //   this will print abcdabc
  //   printf("\n%s", character_array);

  //   there is some risk that a string can be unintentionally changed into a character
  //   array
  // to prevent this, omit the array bound when initializing
  const char always_a_string[] = "abcdefg";
  // this will print abcdefg
  printf("%s", always_a_string);

  // the size of arrays declared using this syntax can be determined at compile time
  // using the sizeof operator
  size_t size = sizeof(always_a_string);

  // if, instead, we declared this string using a pointer as follows:
  const char *foo_ptr = "foo_pointer!";
  // we would need to invoke the strlen function to get the following length, which may
  // incur a runtime cost:
  size_t foo_ptr_size = strlen(foo_ptr) + 1U; // str_len + 1 unsigned
  printf("%lu", foo_ptr_size);
}

int main(void) {
  stringliteral();
  return 0;
}