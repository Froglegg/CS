#include <stdio.h>

int main(void) {

  int a = 1025;
  int *p;
  p = &a;

  printf("Size of integer is %d bytes\n", sizeof(int));
  printf("Address = %d, value is 1025: %d\n", p, *p);

  char *p0;
  p0 = (char *)p; // typecasting int pointer p as pointer to char

  printf("sie of char is %d\n", sizeof(char));
  // the binary of 1025 is
  // 00000000 00000000 00000100 00000001
  // because we assigned p0 to p, typecasted as a char, the compiler only looks for the
  // first byte and does not offset, which will return the value "1" (00000001 is 1 in
  // decimal)
  printf("address is same: %d, but value is 1: %d\n", p0, *p0);
  // incremementing the address by 1 will cause the compiler to look at the next address,
  // again, not offsetting because the type is char
  // b00000100 is 4 in decimal
  printf("address is off by one: %d, but value is 4: %d\n", p0 + 1, *(p0 + 1));

  // void pointer - generic pointer
  void *p1;
  p1 = p;
  // you can not dereference a void pointer, only view the address. That's because
  // there's no type offset that can be looked up for void pointers
  return 0;
}