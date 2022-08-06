#include "collection_internal_header.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This function prints contents of linked list starting from
// the given node
void printList(struct node_type *n) {
  while (n != NULL) {
    printf("\nnode text: %s", n->data.text);
    n = n->next;
  }
}

// modules that implement the ADT (abstract data type) include both the external and
// internal definitions.
int simple_linked_list(void) {

  struct collection_type list;
  list.num_elements = 3;

  struct node_type *head = NULL;
  struct node_type *second = NULL;
  struct node_type *third = NULL;

  // allocate the 3 nodes in the heap
  head = (struct node_type *)malloc(sizeof(struct node_type));
  second = (struct node_type *)malloc(sizeof(struct node_type));
  third = (struct node_type *)malloc(sizeof(struct node_type));

  char head_title[] = "head!";
  char second_title[] = "second!";
  char third_title[] = "third!";
  // use arrow operator to access an element from a pointer to a struct
  strcpy(head->data.text, head_title);
  head->data.size = sizeof(head_title);
  head->next = second;

  strcpy(second->data.text, second_title);
  second->data.size = sizeof(second_title);
  second->next = third;

  strcpy(third->data.text, third_title);
  third->data.size = sizeof(third_title);

  list.head = head;

  printList(list.head);

  free(head);
  free(second);
  free(third);
  return EXIT_SUCCESS;
}

// Set value in list
void setValue(struct node_type *ptr, int i) {
  char title[100];
  sprintf(title, "node: %d", i + 1);
  strcpy(ptr->data.text, title);
  ptr->next = NULL;
}

collection_type circular_linked_list(int num_nodes) {
  struct collection_type dynamic_list;
  dynamic_list.num_elements = num_nodes;

  // create head and tail
  struct node_type *head = NULL;
  struct node_type *tail = NULL;

  for (int i = 0; i < num_nodes; i++) {

    if (i == 0) {
      // create head first
      head = tail = (struct node_type *)malloc(sizeof(struct node_type));
      setValue(tail, i);
    } else {
      // create other nodes
      tail->next = (struct node_type *)malloc(sizeof(struct node_type));
      setValue(tail->next, i);
      tail = tail->next; // update tail pointer
    }
  }

  dynamic_list.head = head;

  return dynamic_list;
}

int main(void) {
  //   simple_linked_list();
  struct collection_type list = circular_linked_list(5);
  printList(list.head);
  free(list.head);
  return EXIT_SUCCESS;
}