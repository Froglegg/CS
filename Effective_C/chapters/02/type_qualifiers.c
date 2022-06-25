// types can be qualified with const, volatile and restrict
// these change behaviors when accessing objects
// note, _Atomic type qualifier is avail since C11 and can support concurrent programs

// const stands for constant, int i cannot be changed, unless you do tricky stuff with
// pointers
const int i = 1;
// volatile objects may change values
volatile int port;
volatile int port = 5000;
// restrict qualifier promotes optimization