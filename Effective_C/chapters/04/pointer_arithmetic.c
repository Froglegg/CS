#include <stdio.h>
// we can perform arithmetic on pointer addresses
int main(void) {

  int arr[100];
  //   for (unsigned int i = 0; i < 99; i++) {
  //     arr[i] = i;
  //     printf("%d\n", arr[i]);
  //   }
  int *arrp1 = &arr[40];
  int *arrp2 = arrp1 + 20; // *arrp2 points to 60
  // prints 20
  printf("%td\n", arrp2 - arrp1);

  return 0;
}