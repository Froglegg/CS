#include <stdio.h>
#include <string.h>

void print(char C[]) {
  int i = 0;
  while (*C != '\0') {
    printf("%c", *C);
    C++;
  }
  printf("\n");
}

int main() {
  char C[] = "Hello";
  print(C);
}