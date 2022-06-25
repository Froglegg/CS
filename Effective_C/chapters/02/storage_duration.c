#include <stdio.h>
// there are four storage durations
// automatic, static, thread and allocated
void incremenet(void) {
  // lifetime of static objects is the entire execution of the program
  // these objects persist after the function has exited
  static unsigned int counter = 0;
  // you could declare counter in file scope which would make it static, however it's
  // better practice to limit scope of objects so we will declare counter as a static
  // unsigned int within our counter function
  counter++;
  printf("%d ", counter);
}

int main(void) {
  // without the "static" storage-class specifier, this would print 1 1 1 1 1
  for (int i = 0; i < 5; i++) {
    incremenet();
  }
  return 0;
}
// thread storage duration is used in concurrent programming and is not covered in this
// book Allocated storage duration deals with dynamically allocated memory and is
// discussed in chapter 6