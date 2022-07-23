#include <limits.h>
#include <stdio.h>

size_t find_element(size_t len, int arr[len], int key) {
  // init and typecast pos as the unsigned long representation of -1;
  size_t pos = (size_t)-1;
  // traverse arr and search for key
  for (size_t i = 0; i < len; ++i) {
    if (arr[i] == key) {
      pos = i;
      break;
    }
  }
  return pos;
}

int absolute_value(int a) { return a < 0 ? -((unsigned int)a) : (unsigned int)a; }

int main(void) {
  int arr[10];
  // arr is 0 - 900
  for (int i = 0; i < 10; ++i) {
    arr[i] = i * 100;
  }
  int key = 9000;
  size_t pos = find_element(sizeof(arr), arr, key);
  if ((int)pos == -1) {
    printf("\n%d not found in array", key);
  } else {
    printf("\nFound %d at position %lu in array", key, pos);
  }

  // abs value of INT_MIN without overflow
  // need to convert to unsigned and also use %u conversion specifier to prevent
  // overflow/wraparound
  printf("\nabsolute value is: %u", absolute_value(INT_MIN));

  return 0;
}