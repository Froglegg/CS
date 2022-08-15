#include <stdio.h>
#include <string.h>

void print(char C[]) {

  int i = 0;
  while (C[i] != '\0') {
    printf("%c", C[i]);
    i++;
  }
  printf("\n");
}

int main() {
  char C[20];
  C[0] = 'J';
  C[1] = 'O';
  C[2] = 'H';
  C[3] = 'N';
  // this will print some garbage at the end because there is no null terminating
  // character
  printf("%s\n", C);
  C[4] = '\0';
  //   this will print correctly
  printf("%s\n", C);
  // this will print length 4, even though we declare length 20 when initializing array,
  // as the null terminating character tells the function when the string is finished
  int length = strlen(C);
  printf("length = %d\n", length);
  // when using string literals, it is not necessary to have a null terminating
  // character, as it is implicit
  // no need to write the size of c when using string literals, as the compiler will
  // implicitly set the size in the main namespace stack frame based on the string
  // literal
  char c_2[] = "Hayes";
  printf("%s\n", c_2);

  char c_3[] = "Hello";
  print(c_3);
}