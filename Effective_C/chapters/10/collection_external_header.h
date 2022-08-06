// this external header implements an opaque or incomplete type to be used as a abstract
// data type in internal header files this assists in separating the interface of the
// collection data abstraction from the implementation of the underlying data strcuture
// which allows the implementation to change without requiring changes to code that
// relies on the collection interface
#include <ctype.h>
// define incomplete type
typedef struct collection_type collection_type;
// function declarations
extern int create_collection(collection_type **result);
extern void destroy_collection(collection_type *col);
extern int add_to_collection(collection_type *col, const void *data, size_t byteCount);
extern int remove_from_collection(collection_type *col, const void *data,
                                  size_t byteCount);
extern int find_in_collection(const collection_type *col, const void *data,
                              size_t byteCount);

