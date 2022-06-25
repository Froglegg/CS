#include <stdio.h>

// object types have alignment requirements that restrict the addresses at which objects
// of that type may be allocated. It represents the number if byters between successive
// addresses typically the compiler will choose alignment requirements for types, however
// you may need to ovverride defaults to meet system-specific requirements using _Alignas

struct S {
  int i;
  double d;
  char c;
};

int main(void) {
  unsigned char bad_buff[sizeof(struct S)];
  _Alignas(struct S) unsigned char good_buff[sizeof(struct S)];

  struct S *bad_s_ptr = (struct S *)bad_buff;   // wrong pointer alignment
  struct S *good_s_ptr = (struct S *)good_buff; // correct pointer alignment
}