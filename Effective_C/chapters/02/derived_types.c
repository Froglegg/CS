#include <stdio.h>
#include <string.h>
// dervied types are constructed from other types
// pointers, arrays, type definitions, structs, and unions

// a pointer type is drgived fromt he funciton or object type that it points to, called
// the referenced type
//  a pointer provides a reference to an entity of the referenced type
int *ip;
char *cp;
void *vp;
// use addresss of & operator to take the address of an object or function
int i = 17;
int *ip = &i;

// an array is a contigously allocated sequence of objects that all have the same type
// array types are cahracterized by type of element as well as number of elements[]
// array of 11 ints
int ia[11];
// array of 17 float pointers
float *afp[17];
// you can use square brackets for index access/setting
void arr_test(void) {
  char str[11];
  for (unsigned int i = 0; i < 10; i++) {
    str[i] = '0' + i;
  };
  str[10] = '\0';
  printf("%s", str);
}

// a structure type contains sequentially allocated objects
// this declares an object identified by sigline that has a type of <struct
// sigrecord> and a pointer to the sigline object identified by sigline_p
struct sigrecord {
  int signum;
  char signame[20];
  char sigdesc[100];
} sigline, *sigline_p;
// the struct has three member objects; signum, and two char arrays (i.e. strings)
// setting and accessing member objects
void test_struct(void) {
  sigline.signum = 5;
  strcpy(sigline.signame, "SIGINT");
  strcpy(sigline.sigdesc, "Interrupt from keyboard");
  // ASSIGN ADDRESS OF SIGNLINE OBJECT TO SIGLINE POINTER
  // using the ampersand use_address_of operator
  // sigline_p = use address of sigline
  sigline_p = &sigline;
  // indirectly access the members of the sigline objects by using the arrow -> operator
  // through the sigline_p pointer
  sigline_p->signum = 5;
  strcpy(sigline_p->signame, "SIGINT");
  strcpy(sigline_p->sigdesc, "Interrupt from keyboard");
}

// union types are similar to structures, except the memory used by the member objects
// overlap unions save memory, can be used to store multiple structs etc.
// this union may be used in a tree or graph that has some nodes that contain integer
// values and others that contain floats
union some_union {
  struct {
    int type;
  } n;
  struct {
    int type;
    int intnode;

  } ni;
  struct {
    int type;
    double doublenode;
  } nf;
} u;

void test_union(void) {
  u.nf.type = 1;
  u.nf.doublenode = 3.14;
}
