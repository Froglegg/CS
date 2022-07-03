#include <stdio.h>
// there are four storage durations
// automatic, static, thread and allocated
u_int16_t increment(void) {
  // lifetime of static objects is the entire execution of the program
  // these objects persist after the function has exited
  static unsigned int counter = 0;
  // you could declare counter in file scope which would make it static, however it's
  // better practice to limit scope of objects so we will declare counter as a static
  // unsigned int within our counter function
  counter++;
  return counter;
}

u_int16_t retrieve(value) { return value; }

int main(void) {
  static unsigned int counter = 0;
  // without the "static" storage-class specifier, this would print 1 1 1 1 1
  for (int i = 0; i < 5; i++) {
    counter = retrieve(increment());
  }
  printf("%d", counter);
  return 0;
}
// thread storage duration is used in concurrent programming and is not covered in this
// book Allocated storage duration deals with dynamically allocated memory and is
// discussed in chapter 6