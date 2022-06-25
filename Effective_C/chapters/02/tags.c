// tags are used to name structs, unions and enums.
// e.g., identifier s for this struct
struct s {
  //
};
// a tag is not a type name and cannot be used to delcare a variable.
// instead, you must declare variables of this type as follows:
struct s v;  // instance of struct s
struct s *p; // pointer to struct s
// same with enums
enum day { sun, mon, tues };
enum day tomorrow;
// can even use same tag as enum type name as they are separate name spaces
// valid, but bad practice probably
enum day day;
// you can think of struct tags as type names and define an alias for the tag by using a
// typedef
typedef struct {
  int x;
} type_alias;
// you can now declare variable of type type_alias instead of struct some_struct
type_alias some_new_int_struct_variable;
void test_type_alias(void) { some_new_int_struct_variable.x = 69; }
// this works fine except for self-referential structs that contain pointers to
// themselves
struct tree_node {
  int count;
  struct tree_node *left;
  struct tree_node *right;
};
// most programmers will just use a typedef and different names for the type nad type
// alias
typedef struct tnode {
  int count;
  struct tnode *left;
  struct tnode *right;
} tree_node;
