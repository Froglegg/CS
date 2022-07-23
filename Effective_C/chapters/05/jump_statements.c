#include <ctype.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// a jump statement unconditionally transfers control to another section of the same
// function when encountered. Lowest level control flow statements and correspond closely
// to the underlying assembly code

// goto statements (can result in spaghetti code)
// any statement can be preceded by a label, which is an identifier followed by a colon
// statements between the goto statement and the label are passed over
// one helpful way to write goto statements is to chain them together to release
// allocated resources when an error occurs and you must leave a function
// resources must be released to prevent leaking
int do_something(void) {
  // this code follows a simple patttern
  // resources are allocated in a certain order, operated upon, and then released in
  // reverse (last in, first out) order. If an error occurs while allocating a resource,
  // the code uses a goto to jump to the appropriate location in cleanup code and
  // rleleases only those resources that have been allocated
  struct object_t {
    int data;
  };

  FILE *file1, *file2;
  struct object_t *obj;
  int ret_val = 0;

  file1 = fopen("a_file", "w");
  if (file1 == NULL) {
    ret_val = -1;
    goto FAIL_FILE1;
  }

  file2 = fopen("another_file", "w");
  if (file2 == NULL) {
    ret_val = -1;
    goto FAIL_FILE2;
  }
  obj = malloc(sizeof(struct object_t));
  if (obj == NULL) {
    ret_val = -1;
    goto FAIL_OBJ;
  }

  // operate on allocated resources

  // clean up everything
  free(obj);

FAIL_OBJ : {
  puts("FAIL OBJ");
  fclose(file2);
}
FAIL_FILE2 : {
  puts("FAIL FILE2");
  fclose(file1);
}
FAIL_FILE1 : {
  puts("FAIL FILE1");
  return ret_val;
}
}

void loop_until_q_is_pressed(void) {
  char c;
  for (;;) {
    puts("Press any Key, Q to quit: ");
    c = toupper(getchar());
    if (strcmp(&c, "q")) {
      puts("WORKED");
      printf("%d", c);
      break;
    }
  }
}

int main(void) {
  do_something();
  loop_until_q_is_pressed();
  // continue jumps to the end of loop body
  // break breaks out of a switch or iteration statement
  // returns just return
  return 0;
}