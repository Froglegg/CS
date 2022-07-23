#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
// memset can be found in string.h
#include <string.h>

void while_statement(unsigned int x) {
  while (x > 0) {
    printf("%d\n", x);
    // prefix decrement operation
    --x;
  }
  return;
}

// memset is a c standard library function that copies the value of val (converted into
// an unsigned char) into each of the first n characters of the objet pointed to by dest
// size_t is a type which is used to represent the size of objects in bytes and is
// therefore used as the return type by the sizeof operator.
void *memset_declaration(void *dest, int val, size_t n) {
  // this line converts dest to a pointer to an unsigned char and assigns the resulting
  // value to ptr. Remember you can do type conversion of an object using (type)object
  // this lets us reserve the value of dest so that it can be returned in the last line

  unsigned char *ptr = (unsigned char *)dest;
  // while loop copies the value of val (converted into unsigned char) into each of the
  // first n characters of the object pointed to by dest.
  while (n-- > 0) {
    *ptr++ = (unsigned char)val;
  }
  return dest;
}

void memset_fun(void) {
  unsigned char dest;
  // use memset to set dest value to each char in ascii unsigned char list 0-127
  for (int i = 0; i < 128; ++i) {
    size_t size_of_val = sizeof(i);
    memset_declaration(&dest, i, size_of_val);
    printf("%c", dest);
  }

  // let's use the string.h memset function ( which has the same implementation as
  // memset_declaration) to copy a character c to the first n lines of a string
  char str[50];
  strcpy(str, "\n\nThis is string.h library function\n");
  puts(str);
  // replace first 7 characters of str with $
  memset(str, '$', 7);
  puts(str);
}

// read from a stream before testing a the state of the stream in I/O
// this code inputs a float quantity, unit of measure (as a string), and an iten name
// (string) from the standard input stream stdin until the end-of-file indicator has been
// set or a read error has occurred
void test_do_while(void) {

  int count;
  float quant;
  char units[21], item[21];

  do {
    // In C language, scanf() function is used to read formatted input from stdin. It
    // returns the whole number of characters written in it otherwise, returns a negative
    // value.
    count = fscanf(stdin, "%f%20s of %20s", &quant, units, item);
    fscanf(stdin, "%*[^\n]");

  } while (!feof(stdin) && ferror(stdin));
}

struct node {
  int data;
  struct node *next;
};
// This function prints contents of linked list starting from
// the given node
void printList(struct node *n) {
  while (n != NULL) {
    printf(" %d ", n->data);
    n = n->next;
  }
}

void singly_linked_list_test(void) {

  struct node head;
  head.data = 0;
  head.next = NULL;

  printList(&head);

  // the following loop is used to deallocate the storage for a linked list
  //   for (ptr = &head; ptr != NULL; ptr = &q) {
  //     q = *ptr->next;
  //     free(ptr);
  //   }
}

int main(void) {
  unsigned int test_int = 10;
  while_statement(test_int);
  memset_fun();

  singly_linked_list_test();

  return 0;
}