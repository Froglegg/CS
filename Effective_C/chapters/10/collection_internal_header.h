#include "collection_external_header.h"

struct data_struct {
  size_t size;
  char text[];
};

struct node_type {
  struct data_struct data;
  size_t size;
  struct node_type *next;
};
// collection type is fully defined but not visible to a user of the data abstraction
struct collection_type {
  size_t num_elements;
  struct node_type *head;
};
