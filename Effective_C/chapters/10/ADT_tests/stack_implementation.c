#include "stack.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// extend stack ADT (StackStruct_t)
struct StackStruct_t {
  int position_current;
  int array[STACK_SIZE];
} StackStruct;

bool StackInit(StackPtr_t Stack) {
  if (Stack != NULL) {
    Stack->position_current = 0;
    return false;
  }
  return true;
}

int StackPush(StackPtr_t Stack, int Item) {
  if (Stack->position_current == STACK_SIZE) {
    return 0;
  } else {
    Stack->array[Stack->position_current] = Item;
    Stack->position_current++;
  }
  return 1;
}

int StackPop(StackPtr_t Stack, int *Item) {
  if (Stack->position_current == STACK_SIZE) {
    return 0;
  } else {
    Stack->position_current--;
    *Item = Stack->array[Stack->position_current];
    return *Item;
  }
}

int main(void) {

  StackPtr_t Stack = malloc(sizeof(StackStruct));

  StackInit(Stack);
  StackPush(Stack, 21);

  int *Item = malloc(sizeof(int));
  int test = StackPop(Stack, Item);

  printf("%d", test);

  // cleanup malloc
  free(Stack);
  free(Item);

  Stack = NULL;
  Item = NULL;

  return EXIT_SUCCESS;
}