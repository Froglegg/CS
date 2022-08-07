// define stack ADT interface
#ifndef STACK_H_
#define STACK_H_

#include <stdbool.h>
// define max size of stack
#define STACK_SIZE 50
// define pointer to ADT
typedef struct StackStruct_t *StackPtr_t;
// define operations
bool StackInit(StackPtr_t Stack);
int StackPush(StackPtr_t, int Item);
int StackPop(StackPtr_t, int *Item);

#endif // STACK_H_
