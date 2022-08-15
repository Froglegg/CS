#include <stdio.h>

void two_dimensional_array(void) {
  int B[2][3];
  B[0][0] = 2;
  B[0][1] = 3;
  B[0][2] = 6;
  B[1][0] = 4;
  B[1][1] = 5;
  B[1][2] = 6;
  // the type of B is three pointers to integer
  int(*p)[3] = B;
  printf("%p\n", p);
  // incrementing the pointer by 1 will increment the address to the next array in the 2D
  // array, i.e., &B[1][0]
  p += 1;
  printf("%p\n", p);
  // decrement to return to first array in 2D array
  p -= 1;
  printf("%p\n", p);
}

// function for three dimensional array
void Func(int (*C)[2][2]) {
  // except first dimension, all other dimensions are enforced
  // this will return address for value 3
  int *address_3 = C[0][1] + 1;
  // print value at address
  printf("%d\n", *address_3);
}

void three_dimensional_array(void) {
  //   int C[3][2][2];
  //   C[0][0][0] = 0;
  //   C[0][0][1] = 1;
  //   C[0][1][0] = 2;
  //   C[0][1][1] = 3;
  //   C[1][0][0] = 4;
  //   C[1][0][1] = 5;
  //   C[1][1][0] = 6;
  //   C[1][1][1] = 7;
  //   C[2][0][0] = 8;
  //   C[2][0][1] = 9;
  //   C[2][1][0] = 10;
  //   C[2][1][1] = 11;

  int C[3][2][2] = {{{0, 1}, {2, 3}}, {{4, 5}, {6, 7}}, {{8, 9}, {10, 11}}};

  // dereference expressions for 3D arrays looks like:
  // C[i][j][k] = *(C[i][j]+k) = *(*(C[i]+j)+k) =
  // *(*(*(C+i)+j)+k)

  // this will return address for value 3
  int *address_3 = C[0][1] + 1;
  // print value at address
  printf("%d\n", *address_3);
  // this will return two pointers to integer at C[1][1] (6)
  int(*address_6)[2] = C[1] + 1;
  // double dereference the pointer to the pointer to get 6
  printf("%d\n", **address_6);
  // passing C into our function, this should print 3
  Func(C);
}

int main(void) {
  three_dimensional_array();

  return 0;
}