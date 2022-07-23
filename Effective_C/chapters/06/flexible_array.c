#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// dynamically allocated arrays with a flexible size are tricky in C
// flexible array members let you declare and allocate storage for a structure with any
// number of fixed members, wher ht elast member is an array of unknown size, aka an
// "incomplete array type", which enables you to

typedef struct {
  size_t num;
  // incomplete array type / flexible array member
  int data[];
} widget;

widget *create_widget_ptr(size_t array_size) {

  // when computing the size of our widget struct containing a flexible array member
  // using the sizeof operator, the flexible array member is ignored.

  // Therefore, we must specifically indlude the apporpriate size for the flexiable array
  // members when allocating storage. To do this, we allocate adidtional bytes for the
  // array member by mulitplying the number of elements in the array member (array_isze)
  // by the size of each element type (sizeof(element_type)).
  widget *p = (widget *)malloc(sizeof(widget) + sizeof(int) * array_size);
  if (p == NULL) {
    return NULL;
  } 

  p->num = array_size;

  return p;
}
int main(void) {
  widget *arr_ptr = create_widget_ptr(100);
  for (size_t i = 0; i < arr_ptr->num; ++i) {
    arr_ptr->data[i] = i;
  }
  for (int i = 0; i < arr_ptr->num; ++i) {
    printf("%d\n", arr_ptr->data[i]);
  }
  return EXIT_SUCCESS;
}